import Vue from "vue";
import VueRouter from "vue-router";
import Lobby from "../views/home/lobby/Lobby";
import HostLobby from "../views/home/create_game/host_lobby/HostLobby";
import JoinGame from "../views/home/JoinGame";
import CreateGame from "../views/home/create_game/CreateGame";
import Admin from "../views/admin/Admin";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: JoinGame
  },
  {
    path: "/Rebecca",
    component: Admin
  },
  {
    path: "/Host",
    component: Admin
  },
  {
    path: "/Admin",
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
  }
];

const router = new VueRouter({
  routes
});

export default router;
