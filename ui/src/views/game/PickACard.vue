<template>
  <div class="pickACard">
    <div v-if="currentView === VIEWS.pickACard">
      <div class="menu-buttons">
        <button
          class="btn-secondary btn-small"
          @click.stop="currentView = VIEWS.viewTableau"
        >
          View Tableaus
        </button>
      </div>

      <div class="score">My Score = {{ currentPlayer.score }}</div>
      <h3>Pick a card</h3>

      <div class="hand">
        <div
          class="card"
          v-for="(card, index) in currentPlayer.hand"
          :key="card.index"
          @click.stop="chooseCard(card, index)"
        >
          <img v-bind:src="card.image" />
          <p class="name">{{ card.name }}</p>
          <p class="hint">{{ card.hint }}</p>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.confirmCard">
      <h3>You want this card?</h3>
      <div class="hand">
        <div class="card-and-description">
          <div class="card">
            <img v-bind:src="pickedCard.image" />
            <p class="name">{{ pickedCard.name }}</p>
            <p class="hint">{{ pickedCard.hint }}</p>
          </div>
          <p class="description">
            {{ pickedCard.description }}
          </p>
        </div>
      </div>

      <div class="confirm-buttons">
        <button class="btn" @click.stop="confirmCard()">Yeah!</button>
        <button class="btn" @click.stop="currentView = VIEWS.pickACard">
          No
        </button>
      </div>
    </div>

    <div v-if="currentView === VIEWS.viewTableau">
      <div class="menu-buttons">
        <button
          class="btn-secondary btn-small"
          @click.stop="currentView = VIEWS.pickACard"
        >
          View Hand
        </button>
      </div>

      <div class="menu-buttons-right">
        <button class="btn-secondary btn-small" @click.stop="previousTableau">
          &lt;-
        </button>

        <button class="btn-secondary btn-small" @click.stop="nextTableau">
          -&gt;
        </button>
      </div>

      <h3>{{ tableauPlayerDisplayName }} tableau</h3>
      <div class="hand">
        <div
          class="card"
          v-for="card in tableauPlayer.tableau"
          :key="card.index"
        >
          <!-- div contents-->
          <img v-bind:src="card.image" />
          <p class="name">{{ card.name }}</p>
          <p class="hint">{{ card.hint }}</p>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.waiting" class="waiting">
      <h3>Waiting for other players to pick cards...</h3>
    </div>

    <div v-if="currentView === VIEWS.newRound">
      <h4>Round {{ round - 1 }} scores:</h4>
      <p v-for="player in players" :key="player.playerName">
        {{ player.playerName }}: {{ player.score }}
      </p>
      <button class="btn btn-secondary" @click="currentView = VIEWS.pickACard">
        Start next round
      </button>
    </div>

    <div v-if="currentView === VIEWS.gameCompleted">
      <h3>Game Completed!</h3>
      <p>Final Scores:</p>
      <p v-for="player in players" :key="player.playerName">
        {{ player.playerName }}: {{ player.score }}
      </p>
      <button class="btn btn-secondary" @click="goHome">
        Exit Game
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
import {findPlayer, findPlayerUnderscore, formatPlayers} from "@/models/Player";
import socket from "@/socket";

export const VIEWS = {
  pickACard: 1,
  confirmCard: 2,
  viewTableau: 3,
  waiting: 4,
  gameCompleted: 5,
  newRound: 6
};

export default {
  data() {
    return {
      currentView: VIEWS.pickACard,
      playerName: Cookies.get("HappyFishCardGame"),
      VIEWS: VIEWS,
      pickedCard: {},
      tableauIndex: 0,
      playerIndex: 0,
      players: [],
      round: 0,
      gameState: ""
    };
  },

  computed: {
    tableauPlayer: function() {
      if (this.players.length === 0) {
        return {};
      }
      return this.players[this.tableauIndex];
    },
    currentPlayer: function() {
      if (this.players.length === 0) {
        return {};
      }
      return this.players[this.playerIndex];
    },
    tableauPlayerDisplayName: function() {
      if (this.tableauPlayer.playerName === this.currentPlayer.playerName) {
        return "My";
      }
      return `${this.players[this.tableauIndex].playerName}'s`;
    }
  },

  async mounted() {
    await this.refreshData();
  },

  methods: {
    refreshData: async function() {
      let self = this;
      let response = await axios.post("http://127.0.0.1:5000/GetGameObject");
      this.gameState = response.data.game_state;
      this.round = response.data.round;
      if (this.gameState === "COMPLETED") {
        await this.handleGameCompleted();
      }
      let players = formatPlayers(response.data.players);
      const { index } = findPlayer(players, self.playerName);
      this.playerIndex = index;
      this.tableauIndex = index;
      this.players = players;
    },

    chooseCard: function(card, index) {
      this.pickedCard = card;
      this.pickedCard.index = index;
      this.currentView = VIEWS.confirmCard;
    },

    confirmCard: function() {
      let self = this;
      axios.post("http://127.0.0.1:5000/PickCard", {
        playerName: self.playerName,
        index: self.pickedCard.index
      });

      self.currentView = VIEWS.waiting;
      socket.on("gameUpdates", payload => {
        const gameUpdates = payload;
        const { player } = findPlayerUnderscore(
          gameUpdates.players,
          this.playerName
        );
        const canPlay = !player.chosen;
        const isNewRound = player.is_new_round;
        this.gameState = gameUpdates.game_state;
        this.round = gameUpdates.round;
        if (this.gameState === "COMPLETED") {
          this.currentView = VIEWS.gameCompleted;
        } else if (canPlay) {
          self.refreshData();
          if (isNewRound) {
            this.currentView = VIEWS.newRound;
          } else {
            this.currentView = VIEWS.pickACard;
          }
        }
        socket.removeAllListeners("gameUpdates");
      });
    },

    nextTableau: function() {
      if (this.tableauIndex + 1 >= this.players.length) {
        this.tableauIndex = 0;
      } else {
        this.tableauIndex++;
      }
    },

    previousTableau: function() {
      if (this.tableauIndex === 0) {
        this.tableauIndex = this.players.length - 1;
      } else {
        this.tableauIndex--;
      }
    },

    goHome: async function() {
      await this.$router.push("/");
    }
  }
};
</script>

<style>
.pickACard {
  text-align: center;
  color: #2c3e50;
}

.hand {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: center;
}

.hand {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: center;
}

.card {
  height: 40%;
  width: 110px;
  margin-top: 10px;
  margin-right: 10px;
  margin-left: 10px;
  text-align: center;
  font-size: 30px;
  background-color: white;
}

.menu-buttons {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: left;
}

.score {
  float: right;
  right: 3px;
  padding-right: 10px;
  padding-top: 10px;
}

.menu-buttons-right {
  float: right;
  right: 1px;
}

.confirm-buttons {
  display: flex;
  justify-content: center;
}

.card-and-description {
  display: flex;
  align-items: center;
}

.name {
  font-family: "Patrick Hand SC", sans-serif;
  font-size: 20px;
  margin: 5px;
}

.hint {
  font-size: 15px;
  margin: 5px;
  font-family: "Patrick Hand SC", sans-serif;
}

.description {
  font-family: "Patrick Hand SC", sans-serif;
  margin: 25px;
  width: 300px;
  font-size: 22px;
}

img {
  height: 80px;
  width: 100px;
}

h3 {
  margin: 0px;
}
</style>
