<template>
  <div class="Lobby">
    <h2>Game Lobby</h2>
    <p style="font-weight: bold">Players: {{ players.length }}</p>
    <p style="font-weight: bold">{{ playerNames }}</p>
    <button @click="resetGame" class="btn yellow-button" style="margin-left:20px;">
      Reset Lobby
    </button>
    <button class="btn purple-button" v-if="gameState === 'NOT_STARTED'" @click="addAiPlayer">
      Add AI Player
    </button>
    <div v-if="gameState === 'ACTIVE'">
      <p>Game is in progress..</p>
    </div>
    <button v-if="gameState === 'NOT_STARTED'" @click="customDeck" class="btn blue-button" style="margin-left:20px;">
      Customize deck
    </button>
    <button v-bind:class="startStyle" @click="StartGame" class="btn pink-button" style="margin-left:20px;">
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
    startable: function() {
      return this.gameState === "NOT_STARTED" && this.playerCount > 1;
    },
    startStyle: function() {
      if (this.startable) {
        return "btn pink-button";
      } else {
        return "btn disabled noHoverStuff";
      }
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
      if (this.startable) {
        await axios.post(`${process.env.VUE_APP_BACKEND_URL}/StartGame`);
        await this.$router.push("PickACard");
      }
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
    async customDeck() {
      await this.$router.push("Deck");
    },
    addAiPlayer: async function() {
      const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/JoinLobby`, {
        playerName: Math.random().toString(),
        is_ai: true
      });
      if (response.data === "Name taken; pick a new name!" || response.data === "Too many players") {
        alert(response.data);
      }
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

.noHoverStuff {
  pointer-events: none;
}
</style>
