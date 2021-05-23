<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      v-if="$router.currentRoute.name !== 'Storefront'"
    >
      <v-btn :to="{ name: 'home' }" icon plain>
        <v-icon>mdi-counter</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <template v-if="!isAuthenticated">
        <v-btn text v-if="!isAuthenticated" :to="{ name: 'login' }"
          >Login</v-btn
        >
      </template>
      <template v-else>
        <span>
          <v-chip color="primary" text-color="white">{{ userEmail }}</v-chip>
          <v-btn text @click="logout()">Logout</v-btn>
        </span>
      </template>
    </v-app-bar>
    <v-main id="main">
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
    ...mapActions("auth", ["logout", "fetchAllStores"]),
    ...mapActions("stores", ["fetchAllStores"]),
  },
  created() {
    this.fetchAllStores()
  }
};
</script>
<style>
#main {
  background-image: url("./assets/wave.svg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: bottom;
}

html {
  overflow-y: auto;
}

::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #010101;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
