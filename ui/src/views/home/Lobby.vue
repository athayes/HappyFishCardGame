<template>
  <div class="Lobby">
    <h3>Lobby 1</h3>
    <p>Players: {{ playerNames }}</p>
    <button v-if="gameState === 'NOT_STARTED'" @click="addAiPlayer" class="btn-secondary">
      Add AI Player
    </button>
    <div v-if="gameState === 'ACTIVE'">
      <p>Game is in progress..</p>
    </div>
    <button v-if="playerCount > 1"
      @click="resetGame"
      class="btn-warning"
    >
      Reset Lobby and Game
    </button>
    <button
      v-if="gameState === 'NOT_STARTED' && playerCount > 1"
      @click="StartGame"
      class="btn-success"
    >
      Start Game
    </button>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
import socket from "@/socket";

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
    },
    playerCount: function() {
      if (this.players) {
        return this.players.length;
      }
      return 0;
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
    let response = await axios.post("http://127.0.0.1:5000/GetLobby");
    this.gameState = response.data.game_state;
    this.players = response.data.players;
  },

  beforeCreate() {
    socket.on("lobbyUpdates", payload => {
      console.log("beforeCreate!");
      console.log(JSON.stringify(payload));
      this.players = payload.players;
      this.gameState = payload.game_state;
    });
  },

  beforeDestroy() {
    socket.removeAllListeners("lobbyUpdates");
  }
};
</script>

<style>
.Lobby {
  text-align: center;
  color: #2c3e50;
}
</style>
