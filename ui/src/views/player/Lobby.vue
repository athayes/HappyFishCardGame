<template>
  <div class="Lobby">
    <h3>Players</h3>
    <div class="userTable paper container container-xs">
      <table class="lobbyTable">
        <tbody>
          <tr v-for="player in players" :key="player">
            <td>{{ player }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <h3>Waiting for x to start the game...</h3>
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
  async created() {
    let self = this;
    let response = await axios.post("http://127.0.0.1:5000/GetPlayersInLobby");
    self.players = response.data.players;

    self.interval = setInterval(async () => {
      let response = await axios.post(
        "http://127.0.0.1:5000/GetPlayersInLobby"
      );
      self.players = response.data.players;
      console.log(response.data.players);
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

.lobbyTable {
  text-align: left;
  font-weight: bold;
}
</style>
