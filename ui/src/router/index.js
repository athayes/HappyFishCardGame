import Vue from "vue";
import VueRouter from "vue-router";
import WaitingForPlayer from "../views/waiting_for_player/WaitingForPlayer";
import ChangeScreenDemo from "../views/change_screen/ChangeScreenDemo";
// import PickACard from "../views/pick_a_card/PickACard";
// import JoinRoom from "../views/join_room/JoinRoom";
// import PickACard from "../views/pick_a_card/PickACard";
import TestSocketIo from "../views/test_socket/TestSocketIo";

Vue.use(VueRouter);

const routes = [
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
    name: "Root",
    component: TestSocketIo
  }
];

const router = new VueRouter({
  routes
});

export default router;
