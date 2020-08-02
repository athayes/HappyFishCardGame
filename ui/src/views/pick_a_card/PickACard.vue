<template>
  <div>
    <div v-if="currentView === VIEWS.pickACard">
      <div class="menu-buttons">
        <button
          class="btn-secondary"
          @click.stop="currentView = VIEWS.viewTableau"
        >
          My Tableau
        </button>
      </div>

      <h3>Pick a card!</h3>
      <div class="hand">
        <div
          class="card"
          v-for="(card, index) in hand"
          :key="card.name"
          @click.stop="chooseCard(card, index)"
        >
          <!-- div contents-->
          <img src="@/assets/egg.png" />
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
          My Tableau
        </button>
      </div>

      <h3>You want this card?</h3>
      <div class="hand">
        <div class="card" @click.stop="confirmCard(card, index)">
          <img src="@/assets/egg.png" />
          <p>{{ pickedCard.name }}</p>
        </div>
        <p class="description">
          This is the description of the card. If it has lots of rules it'd be
          nice to see them :)
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
          class="btn-secondary"
          @click.stop="currentView = VIEWS.pickACard"
        >
          Back
        </button>
      </div>

      <h3>Your tableau</h3>
      <div class="hand">
        <div
          class="card"
          v-for="(card, index) in tableau"
          :key="card.name"
          @click.stop="chooseCard(card, index)"
        >
          <!-- div contents-->
          <img src="@/assets/egg.png" />
          <p>{{ card.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "../../models/Card";
export const VIEWS = {
  pickACard: 1,
  confirmCard: 2,
  viewTableau: 3
};

export default {
  data() {
    return {
      VIEWS: VIEWS,
      currentView: VIEWS.pickACard,
      pickedCard: {},
      hand: [new Card("card1", false), new Card("card2", false)],
      tableau: [new Card("card3", false), new Card("card4", false)]
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

.description {
  width: 20%;
  margin: 20px;
}

.card {
  height: 40%;
  width: 20%;
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
</style>
