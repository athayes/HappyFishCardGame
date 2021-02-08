import Vue from "vue";
import VueRouter from "vue-router";
import Lobby from "../views/player/Lobby";
import HostLobby from "../views/admin/HostLobby";
import JoinLobby from "../views/player/JoinLobby";
import CreateLobby from "../views/admin/CreateLobby";
import Admin from "../views/admin/Admin";
import PickACard from "../views/game/PickACard";
import Home from "../views/Home";
import SetUpTestGame from "@/views/admin/SetUpTestGame";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: Home
  },
  {
    path: "/Host",
    component: Admin
  },
  {
    path: "/CreateLobby",
    component: CreateLobby
  },
  {
    path: "/HostLobby",
    component: HostLobby
  },
  {
    path: "/JoinLobby",
    component: JoinLobby
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
    path: "/SetUpTestGame",
    component: SetUpTestGame
  }
];

const router = new VueRouter({
  routes
});

export default router;
