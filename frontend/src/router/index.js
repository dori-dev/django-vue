import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import About from "../views/AboutView.vue";
import Profile from "../views/ProfileView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: About,
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
