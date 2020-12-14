<template>
  <div class="JoinRoom">
    <h2>Join Game</h2>
    <label for="playerName">Your name</label>
    <input
      v-model="playerName"
      class="JoinGameEnterName"
      type="text"
      id="playerName"
    />
    <button class="btn btn-secondary" @click="joinGame">
      Join Game
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      playerName: ""
    };
  },
  methods: {
    async joinGame() {
      if (this.playerName === "") {
        alert("Enter your name");
        return;
      }

      await axios.post("http://127.0.0.1:5000/JoinGame", {
        playerName: this.playerName
      });
      await this.$router.push("Lobby");
    }
  }
};
</script>

<style>
.JoinRoom {
  text-align: center;
  color: #2c3e50;
}

label {
  text-align: left;
}

.JoinGameEnterName {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
