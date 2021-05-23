<template>
  <v-container fluid>
    <v-row class="text-center">
      <v-col cols="12">
        <v-icon size="200px">mdi-counter</v-icon>
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">Welcome to Countly</h1>
        <p>we will count you</p>

        <p class="subheading font-weight-regular">
          Please select a store that you would like to analize.
        </p>


      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col align-self="center" cols="6">
        <BaseListStores/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import BaseListStores from "@/components/BaseListStores";
export default {
  name: "WelcomePage",
  components: {BaseListStores},
  data: () => ({
    ecosystem: [],
    importantLinks: [],
    whatsNext: [],
  }),
};
</script>
