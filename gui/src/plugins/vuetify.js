import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#80bef5",
        secondary: "#f79f77",
        accent: "#f6d58a",
        info: "#010101",
        error: "#f44336",
        warning: "#ff5722",
        success: "#4caf50",
      },
    },
  },
});
