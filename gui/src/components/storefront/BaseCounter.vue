<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col align-self="center" v-for="(counter, i) in counters" :key="i" cols="1" class="mx-1">
        <FlipCounter
            :value="counter"
            size="100"
            :interval="false"
            mode="up"
        />
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
export default {
  name: "BaseCounter",
  props: {
    currentNumCount: {
      type: Number,
      default: 0,
    }
  },
  data() {
    return {
      value: 100,
      counters: []
    }
  },
  mounted() {
    this.counters = this.currentNumCount.toString().split("").map(num => parseInt(num))
  }
}
</script>

<style scoped>

</style>
