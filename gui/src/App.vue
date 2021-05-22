<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      v-if="$router.currentRoute.name !== 'Storefront'"
    >
      <v-btn :to="{ name: 'home' }" icon>
        <v-icon>mdi-counter</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <template v-if="!isAuthenticated">
        <v-btn text v-if="!isAuthenticated" :to="{ name: 'login' }"
          >Prijava</v-btn
        >
      </template>
      <template v-else>
        <span>
          <v-chip color="primary" text-color="white">{{ userEmail }}</v-chip>
          <v-btn text @click="logout()">odjava</v-btn>
        </span>
      </template>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "App",

  data: () => ({
    //
  }),
  computed: {
    ...mapGetters("auth", ["userEmail", "isAuthenticated"]),
  },
  methods: {
    ...mapActions("auth", ["logout"]),
  },
};
</script>
