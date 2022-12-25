import { createRouter, createWebHashHistory } from "vue-router";
import Lobby from "../views/home/Lobby";
import Join from "../views/home/Join";
import Deck from "../views/deck/Deck";
import PickACard from "../views/game/PickACard";
import Home from "../views/home/Home";

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
    path: "/Join/:id",
    component: Join
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

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
