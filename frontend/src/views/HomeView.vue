<template>
  <div class="home text-start">
    <h1 class="mb-4 text-center">Home</h1>
    <article v-for="article in articles">
      <a :href="`/article/${article.slug}`">
        <h3>
          {{ article.title }}
        </h3>
      </a>
      <div>
        {{ article.description }}
        <a :href="`/article/${article.slug}`">More...</a>
      </div>
      <hr />
    </article>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    let articles = localStorage.getItem("articles");
    articles = JSON.parse(articles);
    return {
      articles: articles,
    };
  },
};
</script>
