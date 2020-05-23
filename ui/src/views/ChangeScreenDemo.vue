<template>
  <div>
    <div>
      <h2>Changing the screen</h2>
      <p>
        We want to change the different screens, e.g loading screen, picking a
        card, totting up the scores at the end of the round etc.
        <br />
        The server will send this client some object and we want to update the
        ui based on that.
        <br />
        I'm using "v-if" to show different components based on a function or
        value, in this case the "getView()" function.
        <br />
        The value of getView() changes based on the value of the timer below.
      </p>
      <p>Timer: {{ timer }}</p>
    </div>
    <div v-if="getView === gameStateEnum.state1">
      <h3>This is the first screen</h3>
    </div>
    <div v-if="getView === gameStateEnum.state2">
      <h3>This is the second screen</h3>
    </div>
    <div v-if="getView === gameStateEnum.state3">
      <h3>This is the third screen</h3>
    </div>
  </div>
</template>

<script>
import { GameStateEnum } from "../models/GameStateEnum";
export default {
  data() {
    return {
      timer: 12,
      gameStateEnum: GameStateEnum
    };
  },
  created() {
    let self = this;
    setInterval(function() {
      if (self.timer <= 1) {
        self.timer = 12;
      }
      self.timer -= 1;
    }, 1000);
  },
  computed: {
    getView: function() {
      if (this.timer < 5) {
        return GameStateEnum.state1;
      }
      if (this.timer < 9) {
        return GameStateEnum.state2;
      }
      if (this.timer < 13) {
        return GameStateEnum.state3;
      }
      return "";
    }
  }
};
</script>

<style></style>
