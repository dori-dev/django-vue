<template>
  <div class="row d-flex justify-content-center">
    <div class="col-md-8 col-12">
      <div class="top-content">
        <h2>Login</h2>
        <p class="heading">
          New user?
          <a class="create-btn d-inline-block">Register</a>
        </p>
      </div>
      <form @submit.prevent="doLogin">
        <div class="inputs mb-4">
          <div class="group mb-3">
            <input
              type="text"
              name="username"
              id="username"
              class="input"
              v-model="username"
            />
            <label for="username" class="input-label username">Username</label>
          </div>
          <div class="group">
            <input
              type="password"
              name="password"
              id="password"
              class="input"
              v-model="password"
            />
            <label for="password" class="input-label password">Password</label>
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
    };
  },
  mounted() {
    let inputs = document.querySelectorAll("input");
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
      console.log(this.username);
      console.log(this.password);
      // this.$store.commit("login", "abc123");
      // this.$router.push("/profile");
    },
  },
};
</script>

<style>
* {
  margin: 0%;
  padding: 0%;
  box-sizing: border-box;
}
body {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}
a {
  text-decoration: none;
  color: #1a73e8;
  display: block;
  font-size: 14px;
}
.top-content {
  text-align: center;
}
img {
  width: 80px;
  margin: 10px 0;
}
h2 {
  font-size: 20px;
  font-weight: 100;
  margin-bottom: 10px;
}
.heading {
  margin-bottom: 30px;
}
input {
  display: block;
  border: 1px solid rgb(228, 228, 228);
  font-size: 16px;
  width: 100%;
  height: 55px;
  padding: 0 15px;
  margin-bottom: 10px;
  position: relative;
  z-index: 2;
  background-color: transparent;
  outline: none;
  border-radius: 5px;
  position: relative;
}
.inputs .group {
  position: relative;
}
.input-label {
  position: absolute;
  top: 15px;
  font-size: 1.1rem;
  left: 14px;
  color: rgb(122, 122, 122);
  font-weight: 100;
  transition: 0.1s ease;
  background-color: white;
  padding: 0 5px;
}
.fill-input-label {
  top: -7px;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
input[type="text"]:focus ~ .input-label.username {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
input[type="text"]:target ~ .input-label.username {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
input[type="password"]:focus ~ .input-label.password {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
input[type="password"]:target ~ .input-label.password {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
.input:focus {
  border: 2px solid #1a73e8;
}
.link-btn {
  margin-bottom: 2rem;
}
.color {
  color: rgb(90, 90, 90);
  font-size: 14px;
  margin-bottom: 5px;
}
.btn-group {
  display: flex;
  justify-content: space-between;
}
.create-btn {
  border: none;
  background-color: transparent;
  color: #1a73e8;
  font-weight: bold;
  cursor: pointer;
  height: 35px;
  padding: 10px 5px;
}
</style>
