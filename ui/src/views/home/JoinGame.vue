<template>
  <div class="JoinRoom">
    <h1>Happy Fish Card Game</h1>
    <p>Enter your name:</p>
    <input class="JoinGameEnterName" type="text" placeholder="" id="name" />
    <br>
    <button class="btn btn-secondary" @click="joinGame">
      Join Game
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    joinGame: function(name) {
      console.log(name);
      let gameId = 1;
      // TODO join the game on the backend
      this.$router.push({
        path: "Lobby",
        query: { gameId: gameId.toString() }
      });
    }
  }
};
</script>

<style>
.JoinRoom {
  text-align: center;
  color: #2c3e50;
}

.JoinGameEnterName {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
