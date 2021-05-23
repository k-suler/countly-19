<template>
  <v-app>
    <v-app-bar
        app
        color="primary"
        dark
        v-if="$router.currentRoute.name !== 'Storefront'"
    >
      <v-btn :to="{ name: 'home' }" icon plain large style="color: #010101">
        <v-icon>mdi-counter</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <template v-if="isAuthenticated">
        <v-tooltip left>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="accent"
                dark
                fab
                small
                style="color: #010101"
                v-bind="attrs"
                v-on="on"
                @click="logout"
            >
              <v-icon>mdi mdi-exit-to-app</v-icon>
            </v-btn>
          </template>
          <span>Logout</span>
        </v-tooltip>

      </template>

      <template v-else>
        <v-btn
            color="accent"
            dark
            style="color: #010101"
            @click="login"
        >
          Login
        </v-btn>
      </template>
    </v-app-bar>
    <v-main id="main">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import {mapGetters, mapActions} from "vuex";

export default {
  name: "App",

  data: () => ({
    fab: false
  }),
  computed: {
    ...mapGetters("auth", ["userEmail", "isAuthenticated"]),
  },
  methods: {
    ...mapActions("auth", ["logout", "fetchAllStores"]),
    ...mapActions("stores", ["fetchAllStores"]),
    login(){
      this.$router.push({name: "login"})
    }
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
