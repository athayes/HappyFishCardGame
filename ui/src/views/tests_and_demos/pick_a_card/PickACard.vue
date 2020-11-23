<template>
  <div class = "pickACard">
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
          <!-- div contents-->
          <img v-bind:src="card.image" />
          <p>{{ card.name }}</p>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.confirmCard">
      <div class="menu-buttons">
        <button
          class="btn-secondary"
          @click.stop="currentView = VIEWS.viewTableau"
        >
          View Tableaus
        </button>
      </div>

      <h3>You want this card?</h3>
      <div class="hand">
        <div class="card" @click.stop="confirmCard(card, index)">
          <img v-bind:src="pickedCard.image" />
          <p>{{ pickedCard.name }}</p>
        </div>
        <p class="description">
          {{  pickedCard.description }}
        </p>

        <div>
          <button class="btn-block">Yeah!</button>
          <br />
          <button class="btn-block" @click.stop="currentView = VIEWS.pickACard">
            No
          </button>
        </div>
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

      <h3>Your tableau</h3>
      <div class="hand">
        <div class="card" v-for="card in tableau" :key="card.name">
          <!-- div contents-->
          <img v-bind:src="card.image" />
          <p>{{ card.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {cardFactory} from "../../../models/Card";
import axios from "axios";
import Cookies from "js-cookie";


export const VIEWS = {
  pickACard: 1,
  confirmCard: 2,
  viewTableau: 3
};

export default {
  data() {
    return {
      playerName: Cookies.get("HappyFishCardGame"),
      VIEWS: VIEWS,
      currentView: VIEWS.pickACard,
      pickedCard: {},
      hand: [],
      tableau: []
    };
  },
  async mounted() {
    let self = this;
    let response = await axios.post("http://127.0.0.1:5000/GetGameObject");
    self.players = response.data.players;
      console.log(response);
      let hand = [];
      let tableau = [];

      for (let card of response.data[self.playerName].hand) {
        hand.push(cardFactory(card.name));
      }

      for (let card of response.data[self.playerName].tableau) {
        tableau.push(cardFactory(card.name));
      }

      self.hand = hand;
      self.tableau = tableau
  },

  methods: {
    chooseCard: function(card, index) {
      console.log(card + index);
      this.pickedCard = card;
      this.currentView = VIEWS.confirmCard;
    },

    confirmCard: function(card) {
      console.log(card.name);
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
  width: 100px;
  margin: 10px;
  text-align: center;
  font-size: 30px;
}

.menu-buttons {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: left;
}

img {
  height: 100px;
  width: 100px;
}

p {
  margin: 10px 0px 10px 0px;
  font-size: 20px;
}

h3 {
  margin: 0px;
}
</style>
