import Vue from "vue";
import VueRouter from "vue-router";
import Lobby from "../views/player/Lobby";
import HostLobby from "../views/admin/HostLobby";
import JoinGame from "../views/player/JoinGame";
import CreateGame from "../views/admin/CreateGame";
import Admin from "../views/admin/Admin";
import PickACard from "../views/tests_and_demos/pick_a_card/PickACard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: JoinGame
  },
  {
    path: "/Host",
    component: Admin
  },
  {
    path: "/CreateGame",
    component: CreateGame
  },
  {
    path: "/HostLobby",
    component: HostLobby
  },
  {
    path: "/JoinGame",
    component: JoinGame
  },
  {
    path: "/Lobby",
    component: Lobby
  },
  {
    path: "/PickACard",
    component: PickACard
  }
];

const router = new VueRouter({
  routes
});

export default router;
