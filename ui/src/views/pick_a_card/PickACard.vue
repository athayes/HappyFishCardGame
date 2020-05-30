<template>
  <div>
    <div class="menu-buttons">
      <span class="badge secondary">My Tableau</span>
      <span class="badge secondary">Game Overview</span>
      <span class="badge secondary">Cheat Sheet</span>
      <span class="badge secondary">Scores</span>
    </div>

    <div v-if="currentView === VIEWS.pickACard">
      <h3>Pick a card!</h3>
      <div class="hand">
        <div
          class="card"
          v-for="(card, index) in hand"
          :key="card.name"
          @click.stop="chooseCard(card, index)"
        >
          <!-- div contents-->
          <p>{{ card.name }}</p>
        </div>
      </div>
    </div>

    <div v-if="currentView === VIEWS.confirmCard">
      <h3>You want this card?</h3>
      <div class="hand">
        <div class="card" @click.stop="confirmCard(card, index)">
          <!-- div contents-->
          <p>{{ pickedCard.name }}</p>
        </div>
        <div>
          <button class="btn-block">Yeah!</button>
          <br />
          <button class="btn-block" @click.stop="currentView = VIEWS.pickACard">
            No
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "../../models/Card";
export const VIEWS = {
  pickACard: 1,
  confirmCard: 2
};

export default {
  data() {
    return {
      VIEWS: VIEWS,
      currentView: VIEWS.pickACard,
      pickedCard: {},
      hand: [new Card("card1", false), new Card("card2", false)]
    };
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
.hand {
  display: flex;
  flex-wrap: nowrap;
  align-items: flex-start;
  justify-content: center;
}

.card {
  height: 40%;
  width: 20%;
  margin: 10px;
  text-align: center;
  font-size: 30px;
}

.menu-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
