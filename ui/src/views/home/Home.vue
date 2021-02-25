<template>
  <div class="Home">
    <h2>Happy Fish Card Game</h2>
    <button class="btn btn-secondary" @click="JoinLobby">
      Join Game
    </button>
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
