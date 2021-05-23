import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import {auth} from "@/firebase/firebase";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";

import ViewStoreFront from "@/views/ViewStoreFront";
import StoreChart from "@/components/StoreChart.vue";
import ViewAllStores from "@/views/ViewAllStores";

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
  { path: "/login", name: "login", component: Login },
  { path: "/store/register", name: "registerStore", component: RegisterStore },
  {
    path: "/chart/:storeId",
    props: true,
    name: "chart",
    component: StoreChart,
  },
  // { path: "/dashboard", component: DashboardPage },
  {
    path: "/storefront",
    name: "Storefront",
    component: ViewStoreFront,
    meta: {
      requiresAuth: true,
    },
  },
    {path: "/signup", name: "signup", component: Signup},
    {path: "/login", name: "login", component: Login},
    {
        path: "/stores",
        name: "stores",
        component: ViewAllStores,
        meta: {
            requiresAuth: true,
        },
    },
    {
        path: "/chart",
        name: "chart",
        component: StoreChart,
        meta: {
            requiresAuth: true,
        },
    },
    {
        path: "/storefront/:storeId",
        props: true,
        name: "Storefront",
        component: ViewStoreFront,
        meta: {
            requiresAuth: true,
        },
    },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((x) => x.meta.requiresAuth);
  if (requiresAuth && !auth.currentUser) {
    next("/login");
  } else {
    next();
  }
});

export default router;
