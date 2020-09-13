<template>
  <div class="Admin">
    <h2>Admin Screen</h2>
    <p>Game not created<button @click="GoToCreatePage">Create Game</button></p>

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
      this.$router.push("CreateGame");
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
