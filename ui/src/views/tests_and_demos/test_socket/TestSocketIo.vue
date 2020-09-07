<template>
  <div class="waiting">
    <h1>Test socket io</h1>
    <button class="btn" @click.stop="connect()">
      Connect
    </button>

    <button class="btn" @click.stop="doThing()">
      Dothing
    </button>
  </div>
</template>

<script>
import io from "socket.io-client";
const socket = io("http://localhost:5000");

socket.on("my_response", data => {
  console.log("recieved response");
  console.log(data);
});

export default {
  methods: {
    connect: async function() {
      if (socket.disconnected) {
        await socket.open();
        console.log("New connection");
      }
      console.log("Already connected");
    },

    doThing: async function() {
      console.log("doing thing");
      await socket.emit("my_message", { hello: "hello" });
    }
  }
};
</script>

<style>
.waiting {
  height: 60vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
