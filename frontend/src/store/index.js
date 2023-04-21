import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
  },
  mutations: {
    onStart(state) {
      let token = localStorage.getItem("token");
      if (token) {
        state.isAuthenticated = true;
        state.token = token;
        axios.defaults.headers.common["Authorization"] = `Token ${token}`;
      } else {
        state.isAuthenticated = false;
        state.token = "";
        axios.defaults.headers.common["Authorization"] = "";
      }
    },
    login(state, token) {
      if (token) {
        state.isAuthenticated = true;
        state.token = token;
        localStorage.setItem("token", token);
        axios.defaults.headers.common["Authorization"] = `Token ${token}`;
      } else {
        state.isAuthenticated = false;
        state.token = "";
        localStorage.removeItem("token");
        axios.defaults.headers.common["Authorization"] = "";
      }
    },
    logout(state) {
      state.isAuthenticated = false;
      state.token = "";
      localStorage.removeItem("token");
      axios.defaults.headers.common["Authorization"] = "";
    },
  },
});
