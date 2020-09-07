<template>
  <div class="Admin">
    <h2>Admin Screen</h2>
    <p>
      Game not started<button>Start game as host</button>
    </p>

    <h3>Advanced stuff</h3>

    <button>Reset Game</button>
      <button>View game object</button>
    <br />
  </div>
</template>

<script>
export default {
  methods: {
    GoToCreatePage: function() {
      let gameId = 1;
      this.$router.push({
        path: "CreateGame",
        query: { gameId: gameId.toString() }
      });
    }
  }
};
</script>

<style>
.Admin {
  text-align: center;
  color: #2c3e50;
}
</style>
