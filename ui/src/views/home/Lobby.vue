<template>
  <div class="Lobby">
    <h2>Lobby</h2>
    <p>Players: {{ players.join(", ") }}</p>
    <button @click="StartGame" class="btn">
      Start Game
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function() {
    return {
      players: [],
      interval: null
    };
  },
  methods: {
    StartGame: async function() {
      await axios.post("http://127.0.0.1:5000/StartGame");
      await this.$router.push("PickACard");
    }
  },
  async created() {
    let self = this;
    let response = await axios.post("http://127.0.0.1:5000/GetLobby");
    self.players = response.data.players;

    self.interval = setInterval(async () => {
      let response = await axios.post(
        "http://127.0.0.1:5000/GetLobby"
      );
      self.players = response.data.players;
    }, 5 * 1000);
  },
  beforeDestroy() {
    clearInterval(this.interval);
  }
};
</script>

<style>
.Lobby {
  text-align: center;
  color: #2c3e50;
}
</style>