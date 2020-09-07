<template>
  <div class="JoinRoom">
    <h2>Join Room: Enter your name</h2>
    <div class="EnterNameWrapper">
      <div class="EnterName">
        <label for="name">Your Name</label>
        <input type="text" placeholder="Rebecca" id="name">

        <button class="btn" @click="joinGame">
          Continue
        </button>
      </div>
    </div>

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
  .EnterName {

    text-align: left;
  }

  .EnterNameWrapper {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
