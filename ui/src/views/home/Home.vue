<template>
  <div class="Home">
    <h2>{{ sillyName }}</h2>
    <label for="name">Your name</label>
    <input
      v-on:keyup.enter="JoinLobby"
      v-model="name"
      class="joinLobbyEnterName"
      type="text"
      id="name"
    />
    <button
      class="btn pink-button"
      @click="CreateRoom"
      style="margin-top:20px;"
    >
      Create Private Room
    </button>
  </div>
</template>

<script>
import { sillyGameName } from "../../models/SillyWords";
import axios from "axios";
import { setCookie } from "../../util/cookies";
import { joinRoom } from "../../socket";

export default {
  data: function() {
    return {
      sillyName: "Happy Fish Card Game",
      name: ""
    };
  },
  methods: {
    async CreateRoom() {
      const name = this.name;
      if (name === "") {
        alert("Enter your name");
        return;
      }
      const response = await axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/CreateLobby`,
        { name: this.name }
      );
      if (
        response.data === "Name taken; pick a new name!" ||
        response.data === "Too many players"
      ) {
        alert(response.data);
      } else {
        const { lobbyId } = response.data;
        setCookie({
          name,
          lobbyId: lobbyId
        });
        await joinRoom({ name, id: lobbyId });
        await this.$router.push(`Lobby`);
      }
    }
  },
  mounted() {
    this.sillyName = sillyGameName();
  }
};
</script>

<style>
.Home {
  text-align: center;
  color: #2c3e50;
  padding: 20px;
}

label {
  text-align: left;
}

.joinLobbyEnterName {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
