<template>
  <v-container fluid>
    <v-row align="center" justify="center" dense no-gutters>
      <v-col align-self="center" v-for="(counter, i) in counters" :key="i" cols="2" class="text-center mx-1">
        <FlipCounter
            :value="counter"
            size="150"
            :interval="false"
            mode="up"
        />
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col align-self="center">
          <h2 class="text-center">
            Number of available spaces
          </h2>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col align-self="center">
        <h4 class="text-center">
          The maximum number of people allowed in this store is {{ maxNumber }}.
        </h4>
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
    },
    maxNumber: {
      type: Number
    }
  },

  computed: {
    counters: function () {
      if (this.currentNumCount < 0){
        return [0]
      } else {
        return  this.currentNumCount.toString().replace("-", "").split("").map(num => parseInt(num))
      }
    }

  }
}
</script>

<style scoped>

</style>
