<template>
  <div class="Home">
    <h2>{{ sillyName }}</h2>
    <button class="btn pink-button" @click="JoinLobby">
      Join Game
    </button>
  </div>
</template>

<script>
import { getRandomItem, sillyWords } from "@/models/SillyWords";

export default {
  data: function() {
    return {
      sillyName: "Happy Fish Card Game"
    };
  },
  methods: {
    async JoinLobby() {
      await this.$router.push("JoinLobby");
    }
  },
  mounted() {
    // eslint-disable-next-line
    this.sillyName = `${getRandomItem(sillyWords.adjectives)} ${getRandomItem(sillyWords.nouns)} ${getRandomItem(sillyWords.adjectives)} Game`;
  }
};
</script>

<style>
.Home {
  text-align: center;
  color: #2c3e50;
}
</style>
