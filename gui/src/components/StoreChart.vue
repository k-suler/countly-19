<template>
  <v-container class="small">
    <v-card class="pa-10">
      <v-row>
        <v-col>Statistics for store: {{ store.name }}</v-col>
        <v-col cols="12">
          <template>
            <line-chart :chart-data="datacollection"></line-chart>
          </template>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import LineChart from "./LineChart.js";
import { database, storesCollection } from "@/firebase/firebase";
import dayjs from "dayjs";

export default {
  components: {
    LineChart,
  },
  props: {
    storeId: String,
  },
  data() {
    return {
      datacollection: {
        labels: [],
        datasets: [
          {
            label: "Number of customers",
            backgroundColor: "#f87979",
            data: [],
          },
        ],
      },
      store: {
        groundTruth: 0,
        startTime: 0,
        description: "",
        name: "",
      },
      timeStep: 5,
    };
  },
  async mounted() {
    if (this.storeId) {
      await storesCollection
        .doc(this.storeId)
        .get()
        .then((res) => {
          this.setData(res.data());
        });
      const vm = this;
      const starCountRef = database
        .ref(`stores/${this.storeId}`)
        .orderByKey()
        .startAt(`${vm.store.startTime.seconds}`);

      starCountRef.on("value", (snapshot) => {
        const data = snapshot.val();
        if (data) {
          this.fillData(data);
        }
      });
    }
  },
  methods: {
    fillData(data) {
      const y = [];
      const x = [];
      const timeNow = Math.floor(Date.now() / 1000);
      let stepCount = this.store.groundTruth;
      for (const [key, value] of Object.entries(data)) {
        if (Math.floor(key / 1000) < timeNow) {
          let label = new Date(Number(key));
          x.push(dayjs(label).format("MM-DD HH:mm"));
          stepCount = stepCount + value;
          y.push(stepCount);
        }
      }

      this.datacollection = {
        labels: x,
        datasets: [
          {
            label: "Number of customers",
            backgroundColor: "#f87979",
            data: y,
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