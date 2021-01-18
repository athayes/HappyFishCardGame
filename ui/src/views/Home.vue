<template>
  <div class="Home">
    <h2>Happy Fish Card Game</h2>
    <button class="btn btn-secondary" @click="JoinLobby">
      Join Game
    </button>
    <p>
      The host of the game should go <router-link to="/Host">here</router-link>
    </p>
  </div>
</template>

<script>

export default {
  methods: {
    async JoinLobby() {
      await this.$router.push("JoinLobby");
    }
  }
};
</script>

<style>
.Home {
  text-align: center;
  color: #2c3e50;
}

</style>
