import mutations from "./mutations.js";
import actions from "./actions.js";
import getters from "./getters.js";

export default {
  namespaced: true,
  state() {
    return {
      tore: {
        name: "",
        description: "",
        maxNumberOfCustomers: "",
        groundTruth: "",
        startTime: ""
      },
      allStores: []
    };
  },
  mutations,
  actions,
  getters,
};
