<template>
  <div class="Admin">
    <h2>Host Menu</h2>
    <button @click="GoToCreatePage">Create Game</button>
    <button>Reset Game</button>
  </div>
</template>

<script>

export default {
  methods: {
    GoToCreatePage: function() {
      this.$router.push("CreateLobby");
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
