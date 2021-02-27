<template>
  <div class="Lobby">
    <h3>Lobby 1</h3>
    <p>Players: {{ playerNames }}</p>
    <button v-if="gameState === 'NOT_STARTED'" @click="addAiPlayer" class="btn">
      Add AI Player
    </button>
    <div v-if="gameState === 'ACTIVE'">
      <p>Game is in progress..</p>
      <button v-if="gameState !== 'COMPLETED'" @click="joinGame" class="btn">
        Join Game
      </button>
    </div>
    <button @click="resetGame" class="btn">
      Reset Lobby and Game
    </button>
    <button v-if="gameState === 'NOT_STARTED'" @click="StartGame" class="btn">
      Start Game
    </button>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";

export default {
  data: function() {
    return {
      players: [],
      interval: null,
      gameState: "",
      playerName: Cookies.get("HappyFishCardGame")
    };
  },
  computed: {
    playerNames: function() {
      if (this.players) {
        return this.players.map(player => player.player_name).join(", ");
      }
      return [];
    }
  },
  methods: {
    StartGame: async function() {
      await axios.post("http://127.0.0.1:5000/StartGame");
      await this.$router.push("PickACard");
    },
    resetGame: async function() {
      await axios.post("http://127.0.0.1:5000/ResetLobbyAndGame");
      await axios.post("http://127.0.0.1:5000/JoinLobby", {
        playerName: this.playerName,
        is_ai: false
      });
    },
    joinGame: async function() {
      await this.$router.push("PickACard");
    },
    addAiPlayer: async function() {
      await axios.post("http://127.0.0.1:5000/JoinLobby", {
        playerName: Math.random().toString(),
        is_ai: true
      });
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
