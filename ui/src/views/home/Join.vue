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
    <button class="btn pink-button" @click="JoinLobby" style="margin-top:20px;">
      Join Game
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
    async JoinLobby() {
      const name = this.name;
      const lobbyId = this.$route.params.id;
      if (name === "") {
        alert("Enter your name");
        return;
      }
      const response = await axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/JoinLobby`,
        { playerName: this.name, lobbyId, is_ai: false }
      );
      if (
        response.data === "Name taken; pick a new name!" ||
        response.data === "Too many players"
      ) {
        alert(response.data);
      } else {
        setCookie({ name, lobbyId });
        await joinRoom({ name, id: lobbyId });
        await this.$router.push("/Lobby");
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
