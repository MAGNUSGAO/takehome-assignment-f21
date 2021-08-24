<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions 
      :complete="true"
    />
    <!-- PART 4: Modify the Show component to accept all of these props -->
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />

    <div class="counter_outer">
      <input type="text" v-model="newShow">
      <button v-on:click="updateState(newShow)" type="button">Add show</button>
    </div>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ]
    };
  },
  methods: {
    updateState(item) {
      console.log("item", item)
      let newShow = {id: this.shows.length, name: item, episodes_seen: 0};
      this.shows.push(newShow)
      console.log(this.shows)
      // this.$shows.push(item)
    },
},
};
</script>

<style>
.counter_outer{
  margin-bottom: 50px;
  margin-left: 20%;
  margin-right: 20%;
  padding: 20px;
  box-shadow: 0 6px 20px rgba(56, 125, 255, 0.17);
    -webkit-filter: drop-shadow(0 6px 20px rgba(56, 125, 255, 0.017));
    filter: drop-shadow(0 6px 20px rgba(56, 125, 255, 0.017));
    border-radius: 2vw;
}
</style>


