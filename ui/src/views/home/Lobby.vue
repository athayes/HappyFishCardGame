<template>
  <div class="Lobby">
    <h2>Game Lobby</h2>
    <p style="font-weight: bold">Players: {{ players.length }}</p>
    <p style="font-weight: bold">{{ playerNames }}</p>
    <button
      @click="resetGame"
      class="btn yellow-button"
      style="margin-left:20px;"
    >
      Reset Lobby
    </button>
    <button
      class="btn purple-button"
      v-if="gameState === 'NOT_STARTED'"
      @click="addAiPlayer"
    >
      Add AI Player
    </button>
    <div v-if="gameState === 'ACTIVE'">
      <p>Game is in progress..</p>
    </div>
    <button
      v-if="gameState === 'NOT_STARTED'"
      @click="customDeck"
      class="btn blue-button"
      style="margin-left:20px;"
    >
      Customize deck
    </button>
    <button
      v-bind:class="startStyle"
      @click="StartGame"
      class="btn pink-button"
      style="margin-left:20px;"
    >
      Join Game
    </button>
  </div>
</template>

<script>
import axios from "axios";
import socket from "../../socket";
import { getCookie } from "../../util/cookies";

export default {
  data: function() {
    return {
      players: [],
      interval: null,
      gameState: "",
      playerName: getCookie().name
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
        await axios.post(`${process.env.VUE_APP_BACKEND_URL}/StartGame`, {
          lobbyId: getCookie().lobbyId
        });
        await this.$router.push("PickACard");
      }
    },
    resetGame: async function() {
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/ResetLobbyAndGame`, {
        lobbyId: getCookie().lobbyId
      });
    },
    joinGame: async function() {
      await this.$router.push("PickACard");
    },
    async customDeck() {
      await this.$router.push("Deck");
    },
    addAiPlayer: async function() {
      const response = await axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/JoinLobby`,
        {
          lobbyId: getCookie().lobbyId,
          playerName: Math.random().toString(),
          is_ai: true
        }
      );
      if (
        response.data === "Name taken; pick a new name!" ||
        response.data === "Too many players"
      ) {
        alert(response.data);
      }
    }
  },
  async created() {
    let response = await axios.post(
      `${process.env.VUE_APP_BACKEND_URL}/GetLobby`,
      { lobbyId: getCookie().lobbyId }
    );
    this.gameState = response.data.game_state;
    this.players = response.data.players;
  },

  beforeCreate() {
    socket.on("lobbyUpdates", payload => {
      const players = payload.players;
      if (this.playerName && !players.includes(this.playerName)) {
        axios.post(`${process.env.VUE_APP_BACKEND_URL}/JoinLobby`, {
          lobbyId: getCookie().lobbyId,
          playerName: this.playerName,
          is_ai: false
        });
      }
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
