import Cookies from "js-cookie";
import store from "../store/index";

export function setCookie(data) {
  Cookies.set("HappyFishCardGame", JSON.stringify(data));
  store.commit("setName", data.name);
  store.commit("setLobbyId", data.lobbyId);
}
