<template>
  <div class="customise-deck">
    <div v-if="view === VIEWS.DECK">
      <h2>Customise Deck</h2>
      <div class="hand">
        <div
          class="card"
          v-bind:style="{ 'background-color': card.backgroundColor }"
          v-for="(card, index) in deck"
          :key="index"
          :class="{ inactive: index === 'cool' }"
          @click.stop="showCards(card.type, index)"
        >
          <div>
            <p class="name">{{ card.type.toLowerCase() }}</p>
            <p class="name">{{ card.name.toLowerCase() }}</p>
            <img v-bind:src="card.image" />
          </div>
        </div>
      </div>
      <button class="pinkish-button btn" @click.stop="finish()">Done</button>
    </div>
    <div v-if="view === VIEWS.CARDS">
      <h2>Pick a card</h2>
      <div class="hand">
        <div
          class="card"
          v-bind:style="{ 'background-color': card.backgroundColor }"
          v-for="(card, index) in temp.cardOptions"
          :key="index"
          :class="{ inactive: index === 'cool' }"
          @click.stop="pickCard(card)"
        >
          <div>
            <p class="name">{{ card.name }}</p>
            <img v-bind:src="card.image" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { EMPTY_DECK, CARD_TYPES, isImmutable } from "../../models/Deck";
import axios from "axios";
import { cardDetails } from "../../models/Card";
import { getCookie } from "../../util/cookies";

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
      temp: {
        cardOptions: [],
        cardIndex: undefined
      }
    };
  },
  methods: {
    showCards: function(type, index) {
      if (isImmutable(type)) {
        alert(`${type} cannot be changed`);
      } else {
        const cardNames = this.deck.map(card => card.name);
        let cards = CARD_TYPES[type].cards.filter(
          card => !cardNames.includes(card)
        );
        cards.push(this.deck[index].name); // allow the currently selected card
        cards = cards.map(card => {
          return {
            name: card,
            image: cardDetails(card).image
          };
        });
        this.temp.cardOptions = cards;
        this.view = VIEWS.CARDS;
        this.temp.cardIndex = index;
      }
    },
    pickCard: function(card) {
      this.deck[this.temp.cardIndex].name = card.name;
      this.deck[this.temp.cardIndex].image = cardDetails(card.name).image;
      this.view = VIEWS.DECK;
      this.temp.cardOptions = [];
    },
    finish: async function() {
      const deck = this.deck;
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/PickDeck`, {
        lobbyId: getCookie().lobbyId,
        deck
      });
      await this.$router.push("Lobby");
    }
  }
};
</script>
