<template>
  <div class="joinRoom">
    <div v-if="currentView === VIEWS.joinOrCreateRoom">
      <h1>Happy Fish Card Game</h1>
      <button class="btn" @click.stop="currentView = VIEWS.createRoomEnterName">
        Create Room
      </button>
      <button class="btn" @click.stop="currentView = VIEWS.joinRoomEnterName">
        Join Room
      </button>
    </div>

    <div v-if="currentView === VIEWS.createRoomEnterName">
      <h2>Create Room</h2>
      <label>Your name</label>
      <div class="enterName">
        <input type="text" placeholder="Name" />
      </div>
      <button class="btn" @click.stop="currentView = VIEWS.createRoom">
        Continue
      </button>
    </div>

    <div v-if="currentView === VIEWS.createRoom">
      <p>Your room name: 1234</p>

      <div class="userTable paper container container-xs">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>Bob Dylan</td>
            </tr>
            <tr>
              <td>2</td>
              <td>Eric Clapton</td>
            </tr>
            <tr>
              <td>3</td>
              <td>Daniel Kahneman</td>
            </tr>
          </tbody>
        </table>
      </div>

      <button class="btn">
        Start Game
      </button>
    </div>

    <div v-if="currentView === VIEWS.joinRoomEnterName">
      <h2>Join Room</h2>
      <label>What is your name?</label>
      <div class="enterName">
        <input type="text" placeholder="Name" />
      </div>

      <button class="btn" @click.stop="currentView = VIEWS.joinRoom">
        Continue
      </button>
    </div>

    <div v-if="currentView === VIEWS.joinRoom">
      <h2>Join Room</h2>
      <label>What is the room code?</label>
      <div class="enterName">
        <input type="text" placeholder="Room Name" />
      </div>

      <button class="btn">
        Enter Room
      </button>
    </div>
  </div>
</template>

<script>
export const VIEWS = {
  joinOrCreateRoom: 1,
  createRoomEnterName: 2,
  createRoom: 3,
  joinRoomEnterName: 4,
  joinRoom: 5
};

export default {
  data() {
    return {
      VIEWS: VIEWS,
      currentView: VIEWS.joinOrCreateRoom
    };
  },

  methods: {
    chooseCard: function(card, index) {
      console.log(card + index);
      this.pickedCard = card;
      this.currentView = VIEWS.confirmCard;
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
