import Vue from "vue";
import VueRouter from "vue-router";
import HomeScreen from "../views/home_screen/HomeScreen";
import Lobby from "../views/home_screen/join_game/lobby/Lobby";
import HostLobby from "../views/home_screen/create_game/host_lobby/HostLobby";
import JoinGame from "../views/home_screen/join_game/JoinGame";
import CreateGame from "../views/home_screen/create_game/CreateGame";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: HomeScreen
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
  }
];

const router = new VueRouter({
  routes
});

export default router;
