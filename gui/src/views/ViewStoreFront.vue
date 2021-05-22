<template>
  <v-container fluid class="fill-height">
    <v-row align="center" justify="start">
      <v-col align-self="center">
        <BlobOrganicCircle/>
      </v-col>
    </v-row>
    <v-row align="center" justify="start">
      <v-col align-self="center">
        <BaseCounter/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import BlobOrganicCircle from "@/components/storefront/BlobOrganicCircle";
import BaseCounter from "@/components/storefront/BaseCounter";
export default {
  name: "ViewStoreFront",
  components: {BaseCounter, BlobOrganicCircle}
}
</script>

<style scoped>

</style>
