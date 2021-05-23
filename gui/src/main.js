import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueFlipCounter from 'vue-flip-counter'
import { auth } from './firebase/firebase.js'
Vue.config.productionTip = false;
Vue.use(VueFlipCounter);

let app
auth.onAuthStateChanged(() => {
    if (!app) {
        app = new Vue({
            router,
            store: store,
            vuetify,
            render: (h) => h(App),
        }).$mount("#app");
    }
})
