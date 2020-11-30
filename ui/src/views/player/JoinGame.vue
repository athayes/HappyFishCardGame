<template>
  <div class="JoinRoom">
    <h1>Happy Fish Card Game</h1>
    <label for="playerName">Your name</label>
    <input
      v-model="name"
      class="JoinGameEnterName"
      type="text"
      id="playerName"
    />
    <br />
    <button class="btn btn-secondary" @click="joinGame">
      Join Game
    </button>

    <br />
    <br />
    <p>
      The host of the game should go <router-link to="/Host">here</router-link>
    </p>
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
