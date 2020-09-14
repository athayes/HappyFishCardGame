<template>
  <div class="Admin">
    <h2>Admin Screen</h2>
    <p>Game not created<button @click="GoToCreatePage">Create Game</button></p>

    <h3>Advanced stuff</h3>

    <button>Reset Game</button>
    <button @click="ViewGameObject">View game object</button>
    <br />
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    GoToCreatePage: function() {
      this.$router.push("CreateGame");
    },
    ViewGameObject: async function() {
      let game = await axios.post("http://127.0.0.1:5000/GetGameObject");
      console.log(JSON.stringify(game));
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
