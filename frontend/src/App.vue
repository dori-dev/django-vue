<template>
  <Navbar />
  <div class="main-content">
    <router-view />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
export default {
  name: "App",
  components: {
    Navbar,
  },
  watch: {
    $route() {
      this.$store.commit("onStart");
    },
  },
  mounted() {
    this.$store.commit("onStart");
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.main-content {
  margin-top: 60px;
  margin-left: 200px;
  padding: 20px;
}
</style>
