<template>
  <v-container fluid class="fill-height">
    <v-row>
      <v-col>
        <v-btn :to="{ name: 'stores'}" icon fab x-large style="color: #010101">
          <v-icon>mdi mdi-arrow-left</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-row align="center" justify="start" dense>
      <v-col align-self="center" class="text-center">
        <h1 v-if="!storeCapacityReached">There is no queue. Come on in!</h1>
        <h1 v-if="storeCapacityReached">There are currently to many people inside. Please wait.</h1>
      </v-col>
    </v-row>
    <v-row align="center" justify="start" dense>
      <v-col align-self="center">
        <BlobOrganicCircle :store-capacity-reached="storeCapacityReached"/>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col>
        <BaseCounter v-if="currentNumCount && doneComputing" :current-num-count="currentNumCount" :max-number="maxNumOfPeople"/>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import BlobOrganicCircle from "@/components/storefront/BlobOrganicCircle";
import BaseCounter from "@/components/storefront/BaseCounter";
import {database, storesCollection} from "@/firebase/firebase"

export default {
  name: "ViewStoreFront",
  components: {BaseCounter, BlobOrganicCircle},
  data() {
    return {
      maxNumOfPeople: 0,
      currentNumCount: null,
      storeCapacityReached: false,
      storeData: {},
      doneComputing: false,
      lastTimeSeen: 0
    }
  },
  props: {
    storeId: {
      type: String,
      required: true,
    }
  },
  async mounted() {
    if (this.storeId) {
      await storesCollection
          .doc(this.storeId)
          .get()
          .then((res) => {
            this.storeData = res.data()
          });
      this.maxNumOfPeople = this.storeData.maxNumberOfCustomers
      this.currentNumCount = this.storeData.maxNumberOfCustomers - this.storeData.groundTruth
      const starCountRef = database
          .ref(`stores/${this.storeId}`)
          .orderByKey()
          .startAt(this.storeData.startTime.seconds + "");
      starCountRef.on("value", (snapshot) => {
        this.doneComputing = false
        const data = snapshot.val();
        this.getCurrentNumOfPeople(data);
      });
    }
  },
  methods: {
    getCurrentNumOfPeople(data) {
      let lTime = this.lastTimeSeen
      for (const [key, value] of Object.entries(data)) {
        lTime = Math.floor(key / 1000)
        if (this.lastTimeSeen < Math.floor(key / 1000)) {
          this.currentNumCount -= value
          this.storeCapacityReached = this.currentNumCount <= 0
        }
      }
      this.lastTimeSeen = lTime
      this.doneComputing = true
    }
  }
}
</script>

<style scoped>

</style>
