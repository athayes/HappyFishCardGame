import io from "socket.io-client";
const socket = io(process.env.VUE_APP_BACKEND_URL);

export async function joinRoom({ name, id }) {
  // leave rooms you're already connected to by disconnecting
  if (socket) {
    await socket.disconnect();
    await socket.connect(process.env.VUE_APP_BACKEND_URL);
  }
  await socket.emit("JOIN_ROOM", { name, id });
}

export default socket;
