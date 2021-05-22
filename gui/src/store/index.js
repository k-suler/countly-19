import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import storesModule from "./modules/stores/index.js";
import authModule from "./modules/auth/index.js";
import storefrontModule from "./modules/storefront/index.js";

export default new Vuex.Store({
  plugins: [createPersistedState()],
  modules: {
    stores: {
      ...storesModule,

      namespaced: true,
    },
    auth: {
      ...authModule,
      namespaced: true,
    },
    storefront: {
      ...storefrontModule,
      namespaced: true
    }
  },
});
