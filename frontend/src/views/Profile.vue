<template>
  <div class="profile text-start">
    <h1>Profile</h1>
    <div
      class="alert alert-danger mt-2"
      style="width: fit-content"
      v-if="profileErr"
    >
      {{ profileErr }}
    </div>
    <div v-if="!profileErr">
      <h4>
        Username:
        <span class="badge bg-primary">{{ username }}</span>
      </h4>
      <h4>
        Email:
        <span class="badge bg-primary">{{ email }}</span>
      </h4>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Profile",
  data() {
    return {
      username: "",
      email: "",
      profileErr: false,
    };
  },
  mounted() {
    this.getInfo();
  },
  methods: {
    getInfo() {
      axios
        .get("/api/auth/users/me/", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          this.profileErr = false;
          let data = response.data;
          this.username = data.username;
          if (data.email) {
            this.email = data.email;
          } else {
            this.email = "none";
          }
        })
        .catch((error) => {
          this.profileErr = "Something wen't wrong to get your profile info.";
          setTimeout(this.getInfo, 5000);
          if (error.response.data.detail) {
            this.$store.commit("logout");
            this.$router.push("/login");
          }
        });
    },
  },
};
</script>
