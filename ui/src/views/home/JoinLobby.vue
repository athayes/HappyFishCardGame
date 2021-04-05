<template>
  <div class="joinRoom">
    <h2>Join Game</h2>
    <label for="playerName">Your name</label>
    <input
      v-model="playerName"
      class="joinLobbyEnterName"
      type="text"
      id="playerName"
    />
    <button
      class="btn pink-button"
      @click="JoinLobby"
      style="margin-top:20px;"
    >
      Join Game
    </button>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";

export default {
  data: function() {
    return {
      playerName: ""
    };
  },
  methods: {
    async JoinLobby() {
      if (this.playerName === "") {
        alert("Enter your name");
        return;
      }

      await axios.post("http://127.0.0.1:5000/JoinLobby", {
        playerName: this.playerName,
        is_ai: false
      });
      Cookies.set("HappyFishCardGame", this.playerName);
      await this.$router.push("Lobby");
    }
  }
};
</script>

<style>
.joinRoom {
  text-align: center;
  color: #2c3e50;
}

label {
  text-align: left;
}

.joinLobbyEnterName {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
