<template>
  <div class="row d-flex justify-content-center">
    <div class="col-md-8 col-12">
      <div class="top-content">
        <h2>Register</h2>
        <p class="heading">
          Have an account?
          <RouterLink to="/login" class="create-btn d-inline-block"
            >Login</RouterLink
          >
        </p>
      </div>
      <form @submit.prevent="doRegister">
        <div class="inputs mb-4">
          <div class="group">
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
          <div class="group mt-3">
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
          <div class="group mt-3">
            <input
              type="password"
              name="password2"
              id="password2"
              class="input form-control"
              v-model="password2"
              :class="{
                'is-invalid': password2Err === true,
                'is-valid': password2Err === false,
              }"
            />
            <label for="password2" class="input-label password"
              >Confirm Password</label
            >
            <div class="invalid-feedback text-start" v-if="password2Err">
              {{ password2Msg }}
            </div>
          </div>
          <a class="create-btn text-start w-100 me-3"> Forgot Password? </a>
        </div>
        <button class="btn btn-primary w-75 mt-3">Create Account</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      usernameErr: null,
      passwordErr: null,
      password2Err: null,
      usernameMsg: "",
      passwordMsg: "",
      password2Msg: "",
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
    doRegister() {
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
      // password2 validation
      this.password2Err = false;
      if (this.password2.length == 0) {
        this.password2Err = true;
        this.password2Msg = "Confirm Password is required.";
      } else if (this.password !== this.password2) {
        this.password2Err = true;
        this.password2Msg = "Passwords do not match.";
      }
      // register
      if (!this.usernameErr & !this.passwordErr & !this.password2Err) {
        axios
          .post("/api/auth/users/", {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            if (response.status === 201) {
              axios
                .post("/api/auth/token/login/", {
                  username: this.username,
                  password: this.password,
                })
                .then((response) => {
                  if (response.status === 200) {
                    let token = response.data.auth_token;
                    this.$store.commit("login", token);
                    this.$router.push("/profile");
                  }
                })
                .catch((error) => {
                  this.$router.push("/login");
                });
            }
          })
          .catch((error) => {
            let data = error.response.data;
            if (data.username) {
              this.usernameErr = true;
              this.usernameMsg = data.username.join(" ");
            } else if (data.password) {
              this.passwordErr = true;
              this.passwordMsg = data.password.join(" ");
            }
          });
      }
    },
  },
};
</script>

<style>
@import "../assets/form.css";
</style>
