<template>
  <div class="HostLobby">
    <h3>Waiting for you to start the game...</h3>
    <div class="userTable paper container container-xs">
      <table class="hostLobbyTable">
        <thead></thead>
        <tbody>
          <tr>
            <td>Bob</td>
          </tr>
          <tr>
            <td>Eric</td>
          </tr>
          <tr>
            <td>Daniel</td>
          </tr>
        </tbody>
      </table>
    </div>

    <button class="btn">
      Start Game
    </button>
  </div>
</template>

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
