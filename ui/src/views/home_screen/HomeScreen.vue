<template>
  <div class="joinRoom">
    <h1>Happy Fish Card Game</h1>
    <div class="userTable paper container container-xs">
      <table>
        <thead>
          <tr>
            <th>Game Name</th>
            <th>Game Host</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="game in games" :key="game.id">
            <td>Game {{ game.id }}</td>
            <td>{{ game.host }}</td>
            <td>
              <button class="btn-block" @click.stop="join(game.id)">
                Join
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <button class="btn" @click.stop="createGame()">
      Create Game
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      games: [{ id: 1, host: "rebecca" }]
    };
  },

  methods: {
    createGame: function() {
      this.$router.push("CreateGame");
    },
    join: function(gameId) {
      this.$router.push({
        path: "JoinGame",
        query: { gameId: gameId.toString() }
      });
    }
  }
};
</script>

<style>
.joinRoom {
  text-align: center;
  color: #2c3e50;
}

.joinRoom table {
  text-align: left;
}

.enterName {
  display: flex;
  justify-content: center;
}
</style>
