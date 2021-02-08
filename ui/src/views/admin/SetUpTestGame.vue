<template>
  <div>
    <h2>Set up test game</h2>
    <button @click="SetUpTestGame" class="btn">
      Set up test game
    </button>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from "js-cookie";

export default {
  methods: {
    SetUpTestGame: async function() {
      await axios.post("http://127.0.0.1:5000/SetUpTestGame");
      Cookies.set("HappyFishCardGame", "reb");
      await this.$router.push("PickACard");
    }
  }
};
</script>

