<template>
  <div class="CreateGame">
    <h2>Create Game</h2>
    <label>Your name</label>
    <input
      v-model="hostName"
      class="CreateGameEnterName"
      type="text"
      placeholder="Name"
    />
    <button @click="createGame()">
      Continue
    </button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: function() {
    return {
      hostName: ""
    };
  },

  methods: {
    createGame: async function() {
      let hostName = this.hostName;
      if (hostName === "") {
        alert("Enter your name");
        return;
      }
      await axios.post('https://localhost:3000/CreateGame', {
        hostName
      });
      await this.$router.push("HostLobby");
    }
  }
};
</script>

<style>
.CreateGame {
  text-align: center;
  color: #2c3e50;
}

.CreateGameEnterName {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
