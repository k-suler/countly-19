import mutations from "./mutations.js";
import actions from "./actions.js";
import getters from "./getters.js";
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default {
  state() {
    return {
      userProfile: {},
    };
  },
  mutations,
  actions,
  getters,
};
