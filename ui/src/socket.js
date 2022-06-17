import io from "socket.io-client";
let socket = io(process.env.VUE_APP_BACKEND_URL);
const JOIN_ROOM = "JOIN_ROOM";

export function joinRoom({ name, id }) {
  socket.emit(JOIN_ROOM, { name, id });
}

export default socket;
