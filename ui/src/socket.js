import io from "socket.io-client";
let socket;

export function joinRoom(id) {
  socket = io(process.env.VUE_APP_BACKEND_URL);
}

export default socket;
