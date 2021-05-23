<template>
  <div class="small">
    <line-chart :chart-data="datacollection"></line-chart>
    <button @click="fillData()">Randomize</button>
  </div>
</template>

<script>
import LineChart from "./LineChart.js";
import { database, storesCollection } from "@/firebase/firebase";

export default {
  components: {
    LineChart,
  },
  data() {
    return {
      datacollection: null,
      store: {
        groundTruth: 0,
        startTime: 0,
        description: "",
        name: "",
      },
      graph: null,
      timeStep: null,
    };
  },
  async mounted() {
    await storesCollection
      .doc("HuTUAOOYnaJMNBxTsf70")
      .get()
      .then((res) => {
        console.log(res.data());
        this.setData(res.data());
      });

    const starCountRef = database
      .ref("stores/HuTUAOOYnaJMNBxTsf70")
      .orderByKey()
      .startAt("1621729668268");
    starCountRef.on("value", (snapshot) => {
      const data = snapshot.val();

      this.fillData(data);
      console.log(data);
    });
  },
  methods: {
    fillData(data) {
      debugger;

      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: "Number of customers",
            backgroundColor: "#f87979",
            data: [this.getRandomInt(), this.getRandomInt()],
          },
        ],
      };
    },
    setData(data) {
      this.store = data;
    },
    makeGraph(timeFrame) {},

    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
  },
};
</script>

<style>
.small {
  max-width: 600px;
  margin: 150px auto;
}
</style>