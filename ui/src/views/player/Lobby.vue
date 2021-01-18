<template>
  <div class="Lobby">
    <h2>Lobby</h2>
    <p>Players: {{ players.join(", ") }}</p>
    <p>Waiting for {{ host_name }} to start the game...</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: function() {
    return {
      players: [],
      interval: null,
      host_name: null
    };
  },
  async created() {
    let self = this;
    let response = await axios.post("http://127.0.0.1:5000/GetLobby");
    self.players = response.data.players;
    self.host_name = response.data.host_name;

    self.interval = setInterval(async () => {
      let response = await axios.post(
        "http://127.0.0.1:5000/GetLobby"
      );
      self.players = response.data.players;
      console.log(response.data);
      if (response.data.is_game_started) {
        clearInterval(this.interval);
        await this.$router.push("PickACard");
      }
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
}

</style>
