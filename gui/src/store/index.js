import Vuex from "vuex";

import authModule from "./modules/auth/index.js";
import storefrontModule from "./modules/storefront/index.js";

export default new Vuex.Store({
  modules: {
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
