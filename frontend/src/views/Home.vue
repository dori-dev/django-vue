<template>
  <div class="home text-start">
    <h1 class="mb-4 text-center">Home</h1>
    <article v-for="article in articles">
      <router-link :to="`/article/${article.slug}`">
        <h3>
          {{ article.title }}
        </h3>
      </router-link>
      <div>
        {{ article.description }}
        <router-link :to="`/article/${article.slug}`">More...</router-link>
      </div>
      <hr />
    </article>
  </div>
  <div class="alert alert-warning" v-if="emptyArticles">
    There is not any articles.
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      articles: [],
      emptyArticles: false,
    };
  },
  mounted() {
    axios
      .get("/api/articles/")
      .then((response) => {
        this.articles = response.data.results;
      })
      .catch((error) => {
        this.articles = [];
        this.emptyArticles = true;
      });
  },
};
</script>
