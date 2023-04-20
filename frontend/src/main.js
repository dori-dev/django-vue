import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "popper.js/dist/popper.min.js";
import "bootstrap/dist/js/bootstrap.min.js";

createApp(App).use(store).use(router).mount("#app");

document.querySelector(".btn-expand-collapse").onclick = function () {
  document.querySelector(".navbar-primary").classList.toggle("collapsed");
};