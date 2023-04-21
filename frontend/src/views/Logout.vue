<template>
  <div class="login">
    <h3 class="mb-4">Are you sure to logout?</h3>
    <button
      class="btn btn-secondary me-3"
      @click="this.$router.push('/profile')"
    >
      Cancle
    </button>
    <button class="btn btn-danger" @click="doLogout">Logout</button>
    <br />
    <div
      class="alert alert-danger mt-5 mx-auto px-3"
      style="width: fit-content"
      v-if="logoutErr"
    >
      {{ logoutErr }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Logout",
  data() {
    return {
      logoutErr: "",
    };
  },
  methods: {
    doLogout() {
      axios
        .post("/api/auth/token/logout/")
        .then((response) => {
          this.$store.commit("logout");
          this.$router.push("/");
        })
        .catch((error) => {
          this.logoutErr = "Something wen't wrong to logging out you.";
        });
    },
  },
};
</script>
