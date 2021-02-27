<template>
  <div class="Lobby">
    <h3>Lobby 1</h3>
    <p>Players: {{ players.join(", ") }}</p>
    <div v-if="gameState === 'ACTIVE'">
      <p>Game is in progress..</p>
      <button v-if="gameState !== 'COMPLETED'" @click="joinGame" class="btn">
        Join Game
      </button>
      <button v-if="gameState !== 'COMPLETED'" @click="StartGame" class="btn">
        Reset Game
      </button>
    </div>
    <button v-if="gameState === 'NOT_STARTED'" @click="StartGame" class="btn">
      Start Game
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      players: [],
      interval: null,
      gameState: "",
    };
  },
  methods: {
    StartGame: async function() {
      await axios.post("http://127.0.0.1:5000/StartGame");
      await this.$router.push("PickACard");
    },
    joinGame: async function() {
      await this.$router.push("PickACard");
    }
  },
  async created() {
    let self = this;
    let response = await axios.post("http://127.0.0.1:5000/GetLobby");
    self.gameState = response.data.game_state;
    self.players = response.data.players;

    self.interval = setInterval(async () => {
      let response = await axios.post(
        "http://127.0.0.1:5000/GetLobby"
      );
      self.players = response.data.players;
    }, 5 * 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  }
};
</script>

<style>
.Lobby {
  text-align: center;
  color: #2c3e50;
}
</style>
