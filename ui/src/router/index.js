import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import WaitingForPlayer from "../views/WaitingForPlayer";
import FunDemo from "../views/ChangeScreenDemo";
import ChangeScreenDemo from "../views/ChangeScreenDemo";

Vue.use(VueRouter);

const routes = [
  {
    path: "/Home",
    name: "Home",
    component: Home
  },
  {
    path: "/WaitingForPlayer",
    name: "Waiting For Player",
    component: WaitingForPlayer
  },
  {
    path: "/ChangeScreenDemo",
    name: "Change Screen Demo",
    component: ChangeScreenDemo
  },
  {
    path: "/",
    name: "Drafting",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Drafting.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;
