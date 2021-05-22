import Vue from "vue";
import Vuex from "vuex";

import authModule from "./modules/auth/index.js";

export default new Vuex.Store({
  modules: {
    auth: {
      ...authModule,
      namespaced: true,
    },
  },
});
