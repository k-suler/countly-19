<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-icon size="200px">mdi-counter</v-icon>
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">Wellcome to Countly</h1>
        <p>we will count you</p>

        <p class="subheading font-weight-regular">
          Please select store that you want to show counter.
        </p>

        <v-btn :to="{ name: 'registerStore' }">Dodaj trgovino</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    ecosystem: [],
    importantLinks: [],
    whatsNext: [],
  }),
};
</script>
