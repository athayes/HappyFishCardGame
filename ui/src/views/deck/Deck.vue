<template>
  <div class="">
    <div v-if="view === VIEWS.DECK">
      <h2>Choose deck</h2>
      <div class="hand">
        <div
          class="card"
          v-bind:style="{ 'background-color': card.backgroundColor }"
          v-for="(card, index) in deck"
          :key="index"
          :class="{ inactive: index === 'cool' }"
          @click.stop="showCards(card.type)"
        >
          <div>
            <p class="name">{{ card.type.toLowerCase() }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="view === VIEWS.CARDS">
      <h2>Pick a card</h2>
      <div class="hand">
        <div
          class="card"
          v-bind:style="{ 'background-color': card.backgroundColor }"
          v-for="(card, index) in cardOptions"
          :key="index"
          :class="{ inactive: index === 'cool' }"
          @click.stop="pickCard(card)"
        >
          <div>
            <p class="name">{{ card }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { EMPTY_DECK, CARD_TYPES, isImmutable } from "../../models/Deck";

const VIEWS = {
  DECK: "deck",
  CARDS: "cards"
};

export default {
  data: function() {
    return {
      VIEWS: VIEWS,
      view: VIEWS.DECK,
      deck: EMPTY_DECK,
      cardOptions: []
    };
  },
  methods: {
    showCards: function(type) {
      if (isImmutable(type)) {
        alert(`${type} cannot be changed`);
      } else {
        this.cardOptions = CARD_TYPES[type].cards;
        this.view = VIEWS.CARDS;
      }
    },
    pickCard: function() {
      this.view = VIEWS.DECK;
      this.cardOptions = [];
    }
  }
};
</script>
