<template>
  <!-- PART 4: Add your code here -->
  <div class="counter_outer">
    <p>{{ name }}</p>
    <Counter
      :count=this.episodes_seen
    />
    
  </div>
</template>

<script>
import Counter from './Counter.vue';
// PART 4: Add your code here
export default {
  components: { Counter },
  props: ['name', 'id', 'episodes_seen'],
  data() {
    return {
      name,
      id: this.id,
      episodes_seen: this.episodes_seen,
    };
  }
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
