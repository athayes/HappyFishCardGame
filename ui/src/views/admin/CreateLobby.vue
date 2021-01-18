<template>
  <div class="CreateLobby">
    <h2>Create Game</h2>
    <label>Your name</label>
    <input
      v-model="hostName"
      class="CreateLobbyEnterName"
      type="text"
      placeholder="Name"
    />
    <button @click="CreateLobby()">
      Continue
    </button>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";

export default {
  data: function() {
    return {
      hostName: ""
    };
  },

  methods: {
    CreateLobby: async function() {
      let hostName = this.hostName;
      if (hostName === "") {
        alert("Enter your name");
        return;
      }
      await axios.post("http://127.0.0.1:5000/CreateLobby", {
        hostName: hostName
      });

      Cookies.set("HappyFishCardGame", hostName);
      await this.$router.push("HostLobby");
    }
  }
};
</script>

<style>
.CreateLobby {
  text-align: center;
  color: #2c3e50;
}

.CreateLobbyEnterName {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
