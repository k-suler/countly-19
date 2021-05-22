import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
// import DashboardPage from "../components/dashboard/dashboard.vue";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";

import RegisterStore from "../components/RegisterStore.vue";
import ViewStoreFront from "@/views/ViewStoreFront";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },

  { path: "/signup", name: "signup", component: Signup },
  { path: "/signin", name: "login", component: Login },
  { path: "/store/register", name: "registerStore", component: RegisterStore },
  // { path: "/dashboard", component: DashboardPage },
  {
    path: "/storefront",
    name: "Storefront",
    component: ViewStoreFront,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
