<template>
  <div class="CreateGame">
    <h2>Create Game</h2>
    <label>Your name</label>
    <div class="enterName">
      <input type="text" placeholder="Name" />
    </div>
    <button @click="createGame('hardcodedname')">
      Continue
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    createGame: function(name) {
      // TODO need to create the game here
      console.log(name);
      let gameId = 1;
      this.$router.push({
        path: "HostLobby",
        query: { gameId: gameId.toString() }
      });
    }
  }
};
</script>

<style>
.CreateGame {
  text-align: center;
  color: #2c3e50;
}
</style>
