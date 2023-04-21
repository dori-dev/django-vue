<template>
  <div class="row d-flex justify-content-center">
    <div class="col-md-8 col-12">
      <div class="top-content">
        <h2>Login</h2>
        <p class="heading">
          New user?
          <router-link to="/register" class="create-btn d-inline-block"
            >Register</router-link
          >
        </p>
      </div>
      <form @submit.prevent="doLogin">
        <div class="inputs mb-4">
          <div class="group mb-3">
            <input
              type="text"
              name="username"
              id="username"
              class="input form-control"
              v-model="username"
              :class="{
                'is-invalid': usernameErr === true,
                'is-valid': usernameErr === false,
              }"
            />
            <label for="username" class="input-label username">Username</label>
            <div class="invalid-feedback text-start" v-if="usernameErr">
              {{ usernameMsg }}
            </div>
          </div>
          <div class="group">
            <input
              type="password"
              name="password"
              id="password"
              class="input form-control"
              v-model="password"
              :class="{
                'is-invalid': passwordErr === true,
                'is-valid': passwordErr === false,
              }"
            />
            <label for="password" class="input-label password">Password</label>
            <div class="invalid-feedback text-start" v-if="passwordErr">
              {{ passwordMsg }}
            </div>
          </div>
          <a class="create-btn text-start w-100 me-3"> Forgot Password? </a>
        </div>
        <button class="btn btn-primary w-75 mt-3">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      usernameErr: null,
      passwordErr: null,
      usernameMsg: "",
      passwordMsg: "",
    };
  },
  mounted() {
    let inputs = document.querySelectorAll(".input");
    inputs.forEach((input) => {
      input.addEventListener("input", (e) => {
        if (input.value.length) {
          input.nextElementSibling.classList.add("fill-input-label");
        } else {
          input.nextElementSibling.classList.remove("fill-input-label");
        }
      });
    });
  },
  methods: {
    doLogin() {
      // username validation
      this.usernameErr = false;
      if (this.username.length <= 3) {
        this.usernameErr = true;
        this.usernameMsg = "Username must be more than 3 characters.";
        if (this.username.length == 0) {
          this.usernameMsg = "Username is required.";
        }
      }
      // password validation
      this.passwordErr = false;
      if (this.password.length < 8) {
        this.passwordErr = true;
        this.passwordMsg = "Password must contain at least 8 characters.";
        if (this.password.length == 0) {
          this.passwordMsg = "Password is required.";
        }
      }
      // login
      if (!this.usernameErr & !this.passwordErr) {
        this.$store.commit("login", `${this.username}:${this.password}`);
        this.$router.push("/profile");
      }
    },
  },
};
</script>

<style>
@import "../assets/form.css";
</style>
