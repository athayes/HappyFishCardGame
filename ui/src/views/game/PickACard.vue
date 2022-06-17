<template>
  <div key="randomKey" class="pickACard" style="margin-top:15px;">
    <div v-if="currentView === VIEWS.pickACard">
      <div class="menu-buttons">
        <button
          class="purple-button btn-small right-side"
          @click.stop="currentView = VIEWS.menu"
        >
          Players
        </button>
      </div>
      <h3>Pick a card</h3>
      <div class="hand">
        <div
          class="card"
          v-bind:style="{ 'background-color': card.backgroundColor }"
          v-for="(card, index) in currentPlayer.hand"
          :key="index + card.name"
          @click.stop="chooseCard(card, index)"
        >
          <img v-bind:src="card.image" />
          <div>
            <p class="name">{{ card.name }}</p>
            <p class="hint">{{ card.hint }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.confirmCard">
      <div class="menu-buttons">
        <button
          class="purple-button btn-small right-side invisible"
          @click.stop="currentView = VIEWS.menu"
        >
          Players
        </button>
      </div>
      <h3>{{ pickedCard.name }}</h3>
      <div class="you-want">
        <div
          class="card"
          v-bind:style="{ 'background-color': pickedCard.backgroundColor }"
        >
          <img v-bind:src="pickedCard.image" />
          <p class="name">{{ pickedCard.name }}</p>
          <p class="hint">{{ pickedCard.hint }}</p>
        </div>
        <p class="description">
          {{ pickedCard.description }}
        </p>
      </div>

      <p>Pick this card?</p>
      <div class="confirm-buttons">
        <button class="pinkish-button btn" @click.stop="confirmCard()">
          OK
        </button>
        <button
          v-if="containsChopsticks"
          class="pinkish-button btn"
          @click.stop="useChopsticks()"
        >
          Pick with Chopsticks
        </button>
        <button
          class="blue-button btn"
          @click.stop="currentView = VIEWS.pickACard"
        >
          Go back
        </button>
      </div>
    </div>

    <div v-if="currentView === VIEWS.waiting" class="waiting">
      <div v-if="showWaitingMessage">
        <button
          class="btn-small invisible"
          @click.stop="currentView = VIEWS.menu"
        >
          Not a real buttton
        </button>
        <h3>Waiting for other players to pick cards...</h3>
      </div>
    </div>

    <div v-if="currentView === VIEWS.newRound">
      <h4>Round {{ round - 1 }} scores:</h4>
      <table style="padding:0px 25%;">
        <tbody>
          <th style="text-align:left;">Player</th>
          <th style="text-align:left;">Score</th>
          <tr v-for="player in players" :key="player.playerName">
            <td style="text-align:left;font-weight:bold;">
              {{ player.playerName }}
            </td>
            <td style="text-align:left;font-weight:bold">{{ player.score }}</td>
          </tr>
        </tbody>
      </table>
      <button class="btn pink-button" @click="currentView = VIEWS.pickACard">
        Start next round
      </button>
      <h4>Score Reports</h4>
      <div v-for="player in players" :key="player.playerName">
        <h4>{{ player.playerName }}</h4>
        <p>Mains: {{ player.scoreReport.tableau.join(", ") }}</p>
        <p v-if="player.dessert.length > 0">
          Desserts: (scored at end of game)
          {{ player.scoreReport.dessert.join(", ") }}
        </p>
        <table>
          <tbody v-if="player.scoreReport">
            <th style="text-align:left;">Card</th>
            <th style="text-align:left;">Score</th>
            <tr
              v-for="(entry, index) in player.scoreReport.report_entries"
              :key="index"
            >
              <td style="text-align:left;">{{ entry.description }}</td>
              <td style="text-align:left;">{{ entry.score }}</td>
            </tr>
            <tr>
              <td style="text-align:left;font-weight:bold">Round total:</td>
              <td style="text-align:left;font-weight:bold">
                {{ player.score - player.scoreReport.score_round_start }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <br />
      <button
        class="btn pink-button btn-bottom"
        @click="currentView = VIEWS.pickACard"
      >
        Start next round
      </button>
      <br />
    </div>

    <div v-if="currentView === VIEWS.gameCompleted">
      <h3>Game Completed!</h3>
      <p>Final Scores:</p>
      <table style="padding:0px 25%;">
        <tbody>
          <tr v-for="player in players" :key="player.playerName">
            <td style="text-align:left;font-style:italic;">
              {{ player.playerName }}
            </td>
            <td style="text-align:left;">{{ player.score }}</td>
          </tr>
        </tbody>
      </table>
      <button class="btn green-button" @click="goHome">Exit Game</button>

      <h4>Score Reports</h4>
      <div v-for="player in players" :key="player.playerName">
        <h4>{{ player.playerName }}</h4>
        <p>Mains: {{ player.scoreReport.tableau.join(", ") }}</p>
        <p v-if="player.scoreReport.dessert.length > 0">
          Desserts: (scored at end of game)
          {{ player.scoreReport.dessert.join(", ") }}
        </p>
        <table>
          <tbody v-if="player.scoreReport">
            <th style="text-align:left;">Card</th>
            <th style="text-align:left;">Score</th>
            <tr
              v-for="(entry, index) in player.scoreReport.report_entries"
              :key="index"
            >
              <td style="text-align:left;">{{ entry.description }}</td>
              <td style="text-align:left;">{{ entry.score }}</td>
            </tr>
            <tr>
              <td style="text-align:left;font-weight:bold">Round total:</td>
              <td style="text-align:left;font-weight:bold">
                {{ player.score - player.scoreReport.score_round_start }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <br />
      <button class="btn green-button btn-bottom" @click="goHome">
        Exit Game
      </button>
      <br />
    </div>

    <div v-if="currentView === VIEWS.menu">
      <div class="menu-buttons">
        <button class="btn-small" @click.stop="currentView = VIEWS.pickACard">
          Back to Game
        </button>
      </div>
      <h3>{{ tableauPlayer.playerName }}</h3>
      <button class="yellow-button btn-small" @click.stop="previousTableau">
        &lt;- Previous
      </button>
      <button class="yellow-button btn-small" @click.stop="nextTableau">
        Next -&gt;
      </button>
      <p>
        <b></b>
      </p>
      <div>
        <div class="collapsible">
          <input
            id="collapsible1"
            type="checkbox"
            checked
            disabled
            name="collapsible"
          />
          <label for="collapsible1">Food</label>
          <div
            v-if="tableauPlayer.tableau.length > 0"
            class="hand collapsible-body"
          >
            <div
              class="card"
              v-bind:style="{ 'background-color': card.backgroundColor }"
              v-for="(card, index) in tableauPlayer.tableau"
              :key="index + card.name"
            >
              <img v-bind:src="card.image" />
              <p class="name">{{ card.name }}</p>
              <p class="hint">{{ card.hint }}</p>
            </div>
          </div>
        </div>

        <div class="collapsible">
          <input
            id="collapsible2"
            type="checkbox"
            checked
            disabled
            name="collapsible"
          />
          <label for="collapsible2">Desserts</label>
          <div
            v-if="tableauPlayer.dessert.length > 0"
            class="hand collapsible-body"
          >
            <div
              class="card"
              v-bind:style="{ 'background-color': card.backgroundColor }"
              v-for="(card, index) in tableauPlayer.dessert"
              :key="index + card.name"
            >
              <img v-bind:src="card.image" />
              <p class="name">{{ card.name }}</p>
              <p class="hint">{{ card.hint }}</p>
            </div>
          </div>
        </div>
      </div>
      <br />
    </div>

    <div v-if="currentView === VIEWS.chopsticksPick">
      <h3>Pick another card</h3>
      <div class="hand">
        <div
          class="card"
          v-bind:style="{ 'background-color': card.backgroundColor }"
          v-for="(card, index) in currentPlayer.hand"
          :key="index + card.name"
          :class="{ inactive: index === chopsticksCard1Index }"
          @click.stop="chopsticksChooseCard(card, index)"
        >
          <img v-bind:src="card.image" />
          <div>
            <p class="name">{{ card.name }}</p>
            <p class="hint">{{ card.hint }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.chopsticksConfirm">
      <h3>{{ pickedCard.name }}</h3>
      <div class="you-want">
        <div
          class="card"
          v-bind:style="{ 'background-color': pickedCard.backgroundColor }"
        >
          <img v-bind:src="pickedCard.image" />
          <p class="name">{{ pickedCard.name }}</p>
          <p class="hint">{{ pickedCard.hint }}</p>
        </div>
        <p class="description">
          {{ pickedCard.description }}
        </p>
      </div>

      <p>Chopsticks: Pick this card as well?</p>
      <div class="confirm-buttons">
        <button class="pinkish-button btn" @click.stop="chopsticksConfirm()">
          OK
        </button>
        <button
          class="blue-button btn"
          @click.stop="currentView = VIEWS.chopsticksPick"
        >
          Go back
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";
import {
  findPlayer,
  findPlayerUnderscore,
  formatPlayers
} from "../../models/Player";
import { getCookie } from "../../util/cookies";
import socket from "../../socket";

export const VIEWS = {
  pickACard: 1,
  confirmCard: 2,
  viewTableau: 3,
  waiting: 4,
  gameCompleted: 5,
  newRound: 6,
  menu: 7,
  desserts: 8,
  chopsticksPick: 9,
  chopsticksConfirm: 10
};

export default {
  data() {
    return {
      // Frontend state
      currentView: VIEWS.pickACard,
      playerName: Cookies.get("HappyFishCardGame"),
      VIEWS: VIEWS,
      pickedCard: {},
      tableauIndex: 0,
      playerIndex: 0,
      // Backend state - game object
      players: [],
      round: 0,
      gameState: "",
      showWaitingMessage: false,
      randomKey: 0,
      chopsticksCard1Index: undefined,
      chopsticksCard2Index: undefined
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
    containsChopsticks: function() {
      const cardNames = this.currentPlayer.tableau.map(card => card.name);
      return !!cardNames.includes("Chopsticks");
    }
  },

  async mounted() {
    console.log("mounted");
    await this.refreshData();
  },

  async activated() {
    console.log("activated");
    await this.refreshData();
  },

  methods: {
    refreshData: async function() {
      let self = this;
      let response;
      try {
        response = await axios.post(
          `${
            process.env.VUE_APP_BACKEND_URL
          }/GetGameObject?timestamp=${new Date().getTime()}`,
          {
            lobbyId: getCookie().lobbyId
          }
        );
      } catch (err) {
        console.log(err);
        await this.goHome();
      }
      if (!response.data.game_state) {
        await this.goHome();
      }
      this.gameState = response.data.game_state;
      this.round = response.data.round;
      if (this.gameState === "COMPLETED") {
        await self.refreshDataGameEnd();
        this.currentView = VIEWS.gameCompleted;
      }
      let players = formatPlayers(response.data.players);
      const { index } = findPlayer(players, self.playerName);
      this.playerIndex = index;
      this.tableauIndex = index;
      this.players = players;
      this.randomKey = new Date().getTime();
    },

    refreshDataGameEnd: async function() {
      let response = await axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/GetLastFinishedGameObject`,
        {
          lobbyId: getCookie().lobbyId
        }
      );
      this.players = formatPlayers(response.data.players);
    },

    chooseCard: function(card, index) {
      this.pickedCard = card;
      this.pickedCard.index = index;
      this.currentView = VIEWS.confirmCard;
    },

    confirmCard: function() {
      let self = this;
      axios.post(`${process.env.VUE_APP_BACKEND_URL}/PickCard`, {
        lobbyId: getCookie().lobbyId,
        playerName: self.playerName,
        index: self.pickedCard.index
      });

      self.startWaitCountDown();
      self.currentView = VIEWS.waiting;
      socket.on("gameUpdates", async payload => {
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
          await self.refreshDataGameEnd();
          this.currentView = VIEWS.gameCompleted;
        } else if (canPlay) {
          await self.refreshData();
          if (isNewRound) {
            this.currentView = VIEWS.newRound;
            socket.removeAllListeners("gameUpdates");
          } else {
            this.currentView = VIEWS.pickACard;
            socket.removeAllListeners("gameUpdates");
          }
        }
      });
    },

    useChopsticks: function() {
      this.chopsticksCard1Index = this.pickedCard.index;
      this.currentView = VIEWS.chopsticksPick;
    },

    chopsticksChooseCard: function(card, index) {
      console.log(this.chopsticksCard1Index);
      if (this.chopsticksCard1Index !== index) {
        this.pickedCard = card;
        this.pickedCard.index = index;
        this.currentView = VIEWS.chopsticksConfirm;
      }
    },

    chopsticksConfirm: function() {
      let self = this;
      axios.post(`${process.env.VUE_APP_BACKEND_URL}/PickCardChopsticks`, {
        lobbyId: getCookie().lobbyId,
        playerName: self.playerName,
        index1: self.chopsticksCard1Index,
        index2: this.pickedCard.index
      });

      self.startWaitCountDown();
      self.currentView = VIEWS.waiting;
      socket.on("gameUpdates", async payload => {
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
          await self.refreshDataGameEnd();
          this.currentView = VIEWS.gameCompleted;
        } else if (canPlay) {
          await self.refreshData();
          if (isNewRound) {
            this.currentView = VIEWS.newRound;
            socket.removeAllListeners("gameUpdates");
          } else {
            this.currentView = VIEWS.pickACard;
            socket.removeAllListeners("gameUpdates");
          }
        }
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
    },

    startWaitCountDown() {
      const self = this;
      self.showWaitingMessage = false;
      setTimeout(() => {
        self.showWaitingMessage = true;
      }, 2000);
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
  justify-content: left;
  padding-bottom: 20px;
}

@media (orientation: portrait) {
  .hand {
    justify-content: center;
  }
}

.you-want {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.card {
  height: 140px;
  width: 110px;
  margin-top: 10px;
  margin-right: 10px;
  margin-left: 10px;
  text-align: center;
  font-size: 30px;
  background-color: white;
  border-color: silver;
}

.menu-buttons {
  text-align: center;
  display: flex;
  justify-content: left;
  padding-right: 30px;
  padding-bottom: 10px;
}

.confirm-buttons {
  display: block;
}

.name {
  font-family: "Patrick Hand SC", sans-serif;
  font-size: 20px;
  margin: 0px;
}

.hint {
  font-size: 14px;
  margin: 5px;
  font-family: "Patrick Hand SC", sans-serif;
}

.description {
  padding-top: 20px;
  padding-left: 40px;
  padding-right: 40px;
  text-align: left;
}

img {
  height: 80px;
  width: 100px;
}

.invisible {
  visibility: hidden;
}

h3 {
  margin: 0px;
}

button {
  margin: 10px;
}

.inactive {
  opacity: 60%;
  border-color: lightgray;
}

.btn-bottom {
  margin-bottom: 10%;
}
</style>
