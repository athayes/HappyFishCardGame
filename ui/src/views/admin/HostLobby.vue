<template>
  <div class="HostLobby">
    <h3>Waiting for you to start the game...</h3>
    <div class="userTable paper container container-xs">
      <table class="hostLobbyTable">
        <thead></thead>
        <tbody>
          <tr v-for="player in players" :key="player">
            <td>{{ player }}</td>
          </tr>
        </tbody>
      </table>
    </div>

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
      players: []
    };
  },
  methods: {
    StartGame: function() {
      this.$router.push("StartGame");
    }
  },
  created() {
    let self = this;
    setInterval(async () => {
      let response = await axios.post("http://127.0.0.1:5000/GetPlayersInLobby");
      self.players = response.data.players;
    }, 5 * 1000);
  }
};
</script>

<style>
.HostLobby {
  text-align: center;
  color: #2c3e50;
}

.hostLobbyTable {
  text-align: left;
  font-weight: bold;
}
</style>
