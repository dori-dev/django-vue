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
</template>

<script>
export default {
  name: "Home",
  data() {
    let articles = localStorage.getItem("articles");
    articles = JSON.parse(articles);
    return {
      articles: articles,
    };
  },
};
</script>
