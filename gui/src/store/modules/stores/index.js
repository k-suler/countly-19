import mutations from "./mutations.js";
import actions from "./actions.js";
import getters from "./getters.js";

export default {
  namespaced: true,
  state() {
    return {
      stores: [
        {
          id: "c1",
          name: "Merkator",
          maxNumberOfCustomers: 100,
          description: "",
        },
      ],
    };
  },
  mutations,
  actions,
  getters,
};
