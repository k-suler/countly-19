import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
// import DashboardPage from "../components/dashboard/dashboard.vue";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },

  { path: "/signup", name: "signup", component: Signup },
  { path: "/signin", name: "login", component: Login },
  // { path: "/dashboard", component: DashboardPage },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
