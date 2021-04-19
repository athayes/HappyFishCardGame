<template>
  <div class="Lobby">
    <h2>Game Lobby</h2>
    <p style="font-weight: bold">Players: {{ playerNames }}</p>
    <button
      class="btn"
      v-if="gameState === 'NOT_STARTED'"
      @click="addAiPlayer"
    >
      Add AI Player
    </button>
    <div v-if="gameState === 'ACTIVE'">
      <p>Game is in progress..</p>
    </div>
    <button
      v-if="playerCount > 1"
      @click="resetGame"
      class="btn purple-button"
      style="margin-left:20px;"
    >
      Reset Lobby and Game
    </button>
    <button
      v-if="gameState === 'NOT_STARTED' && playerCount > 1"
      @click="StartGame"
      class="btn pink-button"
      style="margin-left:20px;"
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
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/StartGame`);
      await this.$router.push("PickACard");
    },
    resetGame: async function() {
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/ResetLobbyAndGame`);
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/JoinLobby`, {
        playerName: this.playerName,
        is_ai: false
      });
    },
    joinGame: async function() {
      await this.$router.push("PickACard");
    },
    addAiPlayer: async function() {
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/JoinLobby`, {
        playerName: Math.random().toString(),
        is_ai: true
      });
    }
  },
  async created() {
    let response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/GetLobby`);
    this.gameState = response.data.game_state;
    this.players = response.data.players;
  },

  beforeCreate() {
    socket.on("lobbyUpdates", payload => {
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
