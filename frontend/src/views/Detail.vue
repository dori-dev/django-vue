<template>
  <div class="home text-start">
    <h1 class="mb-4 text-center">{{ article.title }}</h1>
    <article>
      <div>
        {{ article.description }}
      </div>
      <div>
        Write by <span class="badge bg-primary">{{ article.author }}</span>
      </div>
      <hr />
      <div>
        {{ article.content }}
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: "Detail",
  data() {
    let articles = localStorage.getItem("articles");
    articles = JSON.parse(articles);
    let article = articles.find(
      (element) => element.slug == this.$route.params.slug
    );
    return {
      article: article,
    };
  },
};
</script>
