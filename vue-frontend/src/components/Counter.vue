<template>
<div>
  <p>{{ count }}</p>
  <button v-on:click="count += 1">Increase</button>
  <button v-on:click="count -= 1">Decrease</button>
  <button v-on:click="count = 0">Reset</button>
</div>
  
</template>

<script>
export default {
  props: {
    count: {
      default: 0,
      type: Number
    }
  },
  data() {
    return {
      count
    };
  }
};
</script>

<style>

</style>

