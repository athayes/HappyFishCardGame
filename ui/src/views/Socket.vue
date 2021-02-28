<template>
  <p>hi {{ data }}</p>
</template>
<script>
import io from "socket.io-client";
const socket = io("http://localhost:5000");

export default {
  created() {
    this.timer1();
  },

  data: function() {
    return {
      data: ""
    };
  },
  methods: {
    timer1: async function() {
      socket.on("timer", payload => {
        this.data = payload.timer;
      });
    }
  }
};
</script>
