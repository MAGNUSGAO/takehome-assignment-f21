from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)


@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

# Does the order matter?
# Learned: <x> allows us to pass in a as an argument
@app.route("/shows/<id>", methods=['GET'])
def get_a_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="Sorry show with this ID Does not exist, yet.")
    else:
        return create_response({"shows": db.getById('shows', int(id))})

@app.route("/shows", methods=['POST'])
def post_a_show():
    # Error check
    if not "name" in request.json:
        return create_response(status=422, message="No show name provided")
    elif not "episodes_seen" in request.json:
        return create_response(status=422, message="No Episode watched information provided")

    request.json["episodes_seen"] = int(request.json["episodes_seen"])
    
    db_response = db.create("shows", request.json)
    return create_response(db_response, status=201, message="Successfully inputted show")


# I read partial updates should use PATCH
@app.route("/shows/<id>", methods=['PUT'])
def update_a_show(id):
    # If id cannot be found
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="id not found")
    if not "name" in request.json:
        return create_response(status=422, message="No show name provided")
    elif not "episodes_seen" in request.json:
        return create_response(status=422, message="No Episode watched information provided")

    # Create a new json object with two values only
    temp_json = {}
    temp_json["name"] = request.json["name"]
    temp_json["episodes_seen"] = int(request.json["episodes_seen"])
    
    db_response = db.updateById("shows", int(id), temp_json)
    return create_response(db_response, status=201, message="Successfully updated show")
   
@app.route("/shows", methods=['GET'])
def hello():
    if request.args.get('minEpisodes') is not None:
        return get_shows_with_minEpisodes()
    else:
        return get_all_shows()

def get_all_shows():
    return create_response({"shows": db.get('shows')})

def get_shows_with_minEpisodes():
    min_episodes = int(request.args.get('minEpisodes'))
    all_shows = db.get("shows")
    temp_json = {}
    temp_json["shows"] = []

    for show in all_shows:
        if show["episodes_seen"] >= min_episodes:
            temp_json["shows"].append(show)
    return create_response(temp_json, status=201, message="Successfully retrieved shows")

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
