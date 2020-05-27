<template>
  <div class="drafting">
    <h1>Pick a card!</h1>
    <div class="hand">
      <div
        class="card"
        style="width: 20rem;"
        v-for="(card, index) in hand"
        :key="card.name"
        @click.stop="chooseCard(card, index)"
      >
        <!-- div contents-->
        <p>{{ card.name }}</p>
      </div>
    </div>

    <h1>Your cards:</h1>
    <div class="tableau">
      <div
        class="card"
        style="width: 20rem;"
        v-for="(card, index) in tableau"
        :key="card.name"
        v-bind:class="styleIfChosen(card)"
        @click.stop="returnCard(card, index)"
      >
        <p>{{ card.name }}</p>
      </div>
    </div>

    <br />

    <div class="buttons">
      <button class="btn-large continue-button" @click.stop="okay()">
        Continue
      </button>
    </div>
  </div>
</template>

<script>
import Card from "../models/Card";

export default {
  // Data for the page. If this data changes, the page will update automatically
  data() {
    return {
      hand: [new Card("card1", false), new Card("card2", false)],
      tableau: [
        new Card("card3", true),
        new Card("card4", true),
        new Card("card5", true)
      ],
      cardChosen: false
    };
  },

  methods: {
    // When you select a card
    chooseCard: function(card, index) {
      // "this" is whole component (Drafting)
      if (!this.cardChosen) {
        this.hand.splice(index, 1); // remove the card we chose from the hand
        card.picked = true; // update the style of the card
        this.tableau.push(card);
        this.cardChosen = true;
      }
    },

    // If you return the card
    returnCard: function(card, index) {
      if (this.cardChosen && !card.played) {
        this.tableau.splice(index, 1);
        card.picked = false;
        this.hand.push(card);
        this.cardChosen = false;
      }
    },

    // Update the style of the card if selected
    styleIfChosen(card) {
      return { picked: card.picked };
    },

    // Go to the next page
    okay: function() {
      alert(
        "Continue was pressed. In the real app this would either open a pretty modal, or go to the next page"
      );
    }
  }
};
</script>

<style>
.hand {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: center;
}

.tableau {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: center;
}

.card {
  width: 150px;
  margin: 10px;
  text-align: center;
  line-height: 300px;
  font-size: 30px;
}

.picked {
  background-color: #d3d3d3;
}

.continue-button {
  margin: 90px;
}
</style>
