import Cookies from "js-cookie";

export function setCookie(data) {
  Cookies.set("HappyFishCardGame", JSON.stringify(data));
}

export function getCookie() {
  return JSON.parse(Cookies.get("HappyFishCardGame"));
}
