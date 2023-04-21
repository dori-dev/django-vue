import { createRouter, createWebHistory } from "vue-router";
import store from "../store/index";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Profile from "../views/Profile.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";
import Register from "../views/Register.vue";
import Detail from "../views/Detail.vue";
import Add from "../views/Add.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/article/:slug",
    name: "detail",
    component: Detail,
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
    path: "/add",
    name: "add",
    component: Add,
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
