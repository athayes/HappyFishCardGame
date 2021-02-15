<template>
  <div class="pickACard">
    <div v-if="currentView === VIEWS.pickACard">
      <div class="menu-buttons">
        <button
          class="btn-secondary"
          @click.stop="currentView = VIEWS.viewTableau"
        >
          View Tableaus
        </button>
      </div>

      <h3>Pick a card!</h3>
      <div class="hand">
        <div
          class="card"
          v-for="(card, index) in hand"
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
        <br />
        <button class="btn" @click.stop="currentView = VIEWS.pickACard">
          No
        </button>
      </div>
    </div>

    <div v-if="currentView === VIEWS.viewTableau">
      <div class="menu-buttons">
        <button
          class="btn-secondary btn"
          @click.stop="currentView = VIEWS.pickACard"
        >
          View Hand
        </button>
      </div>

      <div class="menu-buttons-right">
        <button class="btn-secondary btn" @click.stop="previousTableau">
          &lt;-
        </button>

        <button class="btn-secondary btn" @click.stop="nextTableau">
          -&gt;
        </button>
      </div>

      <h3>{{ selectedTableauName }}'s tableau</h3>
      <div class="hand">
        <div class="card" v-for="card in selectedTableau" :key="card.index">
          <!-- div contents-->
          <img v-bind:src="card.image" />
          <p class="name">{{ card.name }}</p>
          <p class="hint">{{ card.hint }}</p>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.waiting" class="waiting">
      <h2>Waiting for other players to pick cards...</h2>
    </div>
  </div>
</template>

<script>
import { cardFactory } from "../../models/Card";
import axios from "axios";
import Cookies from "js-cookie";

export const VIEWS = {
  pickACard: 1,
  confirmCard: 2,
  viewTableau: 3,
  waiting: 4
};

export default {
  data() {
    return {
      currentView: VIEWS.pickACard,
      playerName: Cookies.get("HappyFishCardGame"),
      VIEWS: VIEWS,
      pickedCard: {},
      hand: [],
      tableauList: [],
      selectedTableauIndex: 0
    };
  },

  computed: {
    selectedTableau: function() {
      console.log(this.tableauList[0].tableau);
      return this.tableauList[this.selectedTableauIndex].tableau;
    },

    selectedTableauName: function() {
      return this.tableauList[this.selectedTableauIndex].player;
    }
  },

  async mounted() {
    await this.refreshData();
  },

  methods: {
    chooseCard: function(card, index) {
      this.pickedCard = card;
      this.pickedCard.index = index;
      this.currentView = VIEWS.confirmCard;
    },

    confirmCard: async function() {
      let self = this;
      await axios.post("http://127.0.0.1:5000/PickCard", {
        playerName: self.playerName,
        index: self.pickedCard.index
      });

      self.currentView = VIEWS.waiting;
      self.interval = setInterval(async () => {
        let response = await axios.post("http://127.0.0.1:5000/CanPlayCard", {
          playerName: self.playerName
        });
        let canPlay = response.data["canPlayCard"];
        if (canPlay) {
          clearInterval(self.interval);
          await self.refreshData();
          this.currentView = VIEWS.pickACard;
        }
      }, 5 * 1000);
    },

    refreshData: async function() {
      let self = this;
      let response = await axios.post("http://127.0.0.1:5000/GetGameObject");
      this.players = response.data.players;

      let hand = [];
      for (let card of this.players[self.playerName].hand) {
        hand.push(
          cardFactory(card.name, Object.keys(this.players).length, card.power)
        );
      }
      this.hand = hand;

      let list = [];
      for (let [key, player] of Object.entries(this.players)) {
        let tableau = [];
        let index = 0;
        for (let card of player.tableau) {
          tableau.push(
            cardFactory(card.name, Object.keys(this.players).length, card.power)
          );
        }

        list.push({
          tableau: tableau,
          player: key,
          index: index
        });
        index++;
      }
      this.tableauList = list;

      this.selectedTableauIndex = this.tableauList.findIndex(x => {
        return x.player === self.playerName;
      });
    },

    nextTableau: function() {
      if (this.selectedTableauIndex + 1 >= this.tableauList.length) {
        this.selectedTableauIndex = 0;
      } else {
        this.selectedTableauIndex++;
      }
    },

    previousTableau: function() {
      if (this.selectedTableauIndex === 0) {
        this.selectedTableauIndex = this.tableauList.length - 1;
      } else {
        this.selectedTableauIndex--;
      }
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

.card {
  height: 40%;
  width: 110px;
  margin-top: 10px;
  margin-right: 10px;
  margin-left: 10px;
  text-align: center;
  font-size: 30px;
}

.menu-buttons {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: left;
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
