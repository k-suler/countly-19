import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import authModule from "./modules/auth/index.js";

export default new Vuex.Store({
    plugins: [createPersistedState()],
  modules: {
    auth: {
      ...authModule,
      namespaced: true,
    },
  },
});
