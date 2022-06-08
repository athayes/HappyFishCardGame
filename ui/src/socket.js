import io from "socket.io-client";
const socket = io(process.env.VUE_APP_BACKEND_URL);

export function joinRoom(id) {
  socket.on("connection", socket => {
    socket.join(id);
  });
}

export default socket;
