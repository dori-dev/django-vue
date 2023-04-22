<template>
  <div class="row d-flex justify-content-center">
    <div class="col-md-8 col-12">
      <div class="top-content">
        <h2>Add an article</h2>
        <p class="heading">
          An idea to create an article?
          <router-link to="/" class="create-btn d-inline-block"
            >Home</router-link
          >
        </p>
      </div>
      <div class="alert alert-danger mb-4 text-start" v-if="error">
        Something wen't wrong to create the article.
      </div>
      <form @submit.prevent="createArticle">
        <div class="inputs mb-4">
          <div class="group">
            <input
              type="text"
              name="title"
              id="title"
              class="input form-control"
              v-model="title"
              :class="{
                'is-invalid': titleErr === true,
                'is-valid': titleErr === false,
              }"
            />
            <label for="title" class="input-label title">Title</label>
            <div class="invalid-feedback text-start" v-if="titleErr">
              {{ titleMsg }}
            </div>
          </div>
          <div class="group mt-3">
            <input
              type="text"
              name="description"
              id="description"
              class="input form-control"
              v-model="description"
              :class="{
                'is-invalid': descriptionErr === true,
                'is-valid': descriptionErr === false,
              }"
            />
            <label for="description" class="input-label description"
              >Description</label
            >
            <div class="invalid-feedback text-start" v-if="descriptionErr">
              {{ descriptionMsg }}
            </div>
          </div>
          <div class="group mt-3">
            <textarea
              class="input form-control"
              name="content"
              id="content"
              rows="10"
              v-model="content"
              :class="{
                'is-invalid': contentErr === true,
                'is-valid': contentErr === false,
              }"
            >
            </textarea>
            <label for="content" class="input-label content">Content</label>
            <div class="invalid-feedback text-start" v-if="contentErr">
              {{ contentMsg }}
            </div>
          </div>
        </div>
        <button class="btn btn-primary w-75 mt-3 mb-5">Create Article</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Add",
  data() {
    return {
      title: "",
      description: "",
      content: "",
      titleErr: null,
      descriptionErr: null,
      contentErr: null,
      titleMsg: "",
      descriptionMsg: "",
      contentMsg: "",
      error: false,
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
    createArticle() {
      // title validation
      this.titleErr = false;
      if (this.title.length === 0) {
        this.titleErr = true;
        this.titleMsg = "Title is required.";
      }
      // description validation
      this.descriptionErr = false;
      if (this.description.length === 0) {
        this.descriptionErr = true;
        this.descriptionMsg = "Description is required.";
      }
      // content validation
      this.contentErr = false;
      if (this.content.length === 0) {
        this.contentErr = true;
        this.contentMsg = "Content is required.";
      }
      // add
      if (!this.titleErr & !this.descriptionErr & !this.contentErr) {
        let article = {
          title: this.title,
          description: this.description,
          content: this.content,
        };
        axios
          .post("/api/articles/", article)
          .then((response) => {
            if (response.status === 201) {
              let slug = response.data.slug;
              if (slug) {
                this.$router.push(`/article/${slug}`);
              } else {
                this.error = true;
              }
            } else {
              this.error = true;
            }
          })
          .catch((error) => {
            this.error = true;
          });
      }
    },
  },
};
</script>

<style>
@import "../assets/form.css";
</style>
