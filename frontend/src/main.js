import { createApp } from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "popper.js/dist/popper.min.js";
import "bootstrap/dist/js/bootstrap.min.js";

createApp(App).use(store).use(router).mount("#app");

axios.defaults.baseURL = "http://127.0.0.1:8000";
