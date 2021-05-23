<template>
  <v-container fluid class="fill-height">
    <v-row align="center" justify="start">
      <v-col align-self="center">
        <BlobOrganicCircle/>
      </v-col>
    </v-row>
    <v-row dense>
      <v-col>
        <BaseCounter :currentNumCount="currentNumCount"/>
      </v-col>
    </v-row>
    <v-row align="center" justify="center" dense>
      <v-col align-self="center">
        <div class="text-center">
          The maximum number of people allowed in this store is {{ maxNumOfPeople }}.
        </div>
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
      maxNumOfPeople: 10,
      currentNumCount: 100,
      storeId: null
    }
  },
  created() {
    this.storeId = this.$route.query.storeId
  },
  mounted() {
    if (this.storeId) {
      storesCollection.doc(`${this.storeId}`).get().then((res) => {
        console.log(res.data())
      })

      const starCountRef = database.ref(`stores/${this.storeId}`).orderByKey().startAt("1621723610")
      starCountRef.on('value', (snapshot) => {
        const data = snapshot.val();
        console.log(data)
      });
    }


  }
}
</script>

<style scoped>

</style>
