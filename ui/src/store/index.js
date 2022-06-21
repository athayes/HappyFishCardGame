import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    name: "",
    lobbyId: ""
  },
  mutations: {
    setName(state, name) {
      state.name = name;
    },
    setLobbyId(state, lobbyId) {
      state.lobbyId = lobbyId;
    }
  }
});
