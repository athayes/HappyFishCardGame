import Vue from "vue";
import VueRouter from "vue-router";
import Lobby from "../views/home/Lobby";
import Deck from "../views/deck/Deck";
import PickACard from "../views/game/PickACard";
import Home from "../views/home/Home";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: Home
  },
  {
    path: "/Lobby",
    component: Lobby
  },
  {
    path: "/PickACard",
    component: PickACard
  },
  {
    path: "/Deck",
    component: Deck
  }
];

const router = new VueRouter({
  routes
});

export default router;
