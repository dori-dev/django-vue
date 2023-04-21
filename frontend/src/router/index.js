import { createRouter, createWebHistory } from "vue-router";
import store from "../store/index";
import HomeView from "../views/HomeView.vue";
import About from "../views/AboutView.vue";
import Profile from "../views/ProfileView.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";
import Register from "../views/Register.vue";

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
    meta: {
      loginRequired: true,
    },
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      loginRedirect: true,
    },
  },
  {
    path: "/register",
    name: "register",
    component: Register,
    meta: {
      loginRedirect: true,
    },
  },
  {
    path: "/logout",
    name: "logout",
    component: Logout,
    meta: {
      loginRequired: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.loginRequired)) {
    if (store.state.isAuthenticated) {
      next();
    } else {
      next("/login");
    }
  } else if (to.matched.some((record) => record.meta.loginRedirect)) {
    if (store.state.isAuthenticated) {
      next("/profile");
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
