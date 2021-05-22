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

export default {
  name: "ViewStoreFront",
  components: {BaseCounter, BlobOrganicCircle},
  data() {
    return {
      maxNumOfPeople: 10,
      currentNumCount: 100
    }
  },
}
</script>

<style scoped>

</style>
