<template>
  <div class="content" v-if="!articleError">
    <div class="home text-start">
      <h1 class="mb-4 text-center">{{ article.title }}</h1>
      <article>
        <div>
          {{ article.description }}
        </div>
        <div>
          Write by <span class="badge bg-primary">{{ article.author }}</span>
        </div>
        <div
          class="alert alert-warning mt-3"
          style="width: fit-content"
          v-if="deleteError"
        >
          Something wen't wrong to delete this article.
        </div>
        <div
          class="col-md-5 col-12 d-flex justify-content-start mt-3"
          v-if="$store.state.isAuthenticated & canEdit"
        >
          <button class="btn btn-primary btn-sm me-3 col-5" @click="changeEdit">
            <svg
              class="btn-icon"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
            >
              <path
                d="M497.9 74.16L437.8 14.06c-18.75-18.75-49.19-18.75-67.93 0l-56.53 56.55l127.1 128l56.56-56.55C516.7 123.3 516.7 92.91 497.9 74.16zM290.8 93.23l-259.7 259.7c-2.234 2.234-3.755 5.078-4.376 8.176l-26.34 131.7C-1.921 504 7.95 513.9 19.15 511.7l131.7-26.34c3.098-.6191 5.941-2.141 8.175-4.373l259.7-259.7L290.8 93.23z"
              />
            </svg>
            Edit
          </button>
          <button class="btn btn-danger btn-sm col-5" @click="removeArticle">
            <svg
              class="btn-icon"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 448 512"
            >
              <path
                d="M32 464C32 490.5 53.5 512 80 512h288c26.5 0 48-21.5 48-48V128H32V464zM304 208C304 199.1 311.1 192 320 192s16 7.125 16 16v224c0 8.875-7.125 16-16 16s-16-7.125-16-16V208zM208 208C208 199.1 215.1 192 224 192s16 7.125 16 16v224c0 8.875-7.125 16-16 16s-16-7.125-16-16V208zM112 208C112 199.1 119.1 192 128 192s16 7.125 16 16v224C144 440.9 136.9 448 128 448s-16-7.125-16-16V208zM432 32H320l-11.58-23.16c-2.709-5.42-8.25-8.844-14.31-8.844H153.9c-6.061 0-11.6 3.424-14.31 8.844L128 32H16c-8.836 0-16 7.162-16 16V80c0 8.836 7.164 16 16 16h416c8.838 0 16-7.164 16-16V48C448 39.16 440.8 32 432 32z"
              />
            </svg>
            Remove
          </button>
        </div>
        <hr />
        <div v-if="!edit" style="white-space: pre-line">
          {{ article.content }}
        </div>
      </article>
    </div>
    <div class="row d-flex justify-content-start" v-if="edit">
      <div class="col-md-8 col-12">
        <div class="alert alert-warning text-start" v-if="updateError">
          Something wen't wrong to update article.
        </div>
        <form @submit.prevent="updateArticle">
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
              <label for="title" class="input-label title fill-input-label"
                >Title</label
              >
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
              <label
                for="description"
                class="input-label description fill-input-label"
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
              <label for="content" class="input-label content fill-input-label"
                >Content</label
              >
              <div class="invalid-feedback text-start" v-if="contentErr">
                {{ contentMsg }}
              </div>
            </div>
          </div>
          <button class="btn btn-primary w-75 mt-3 mb-5">Update Article</button>
        </form>
      </div>
    </div>
  </div>
  <div class="alert alert-danger" v-if="articleError">
    Article not found (404)
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Detail",
  data() {
    return {
      article: {},
      canEdit: false,
      title: "",
      description: "",
      content: "",
      titleErr: null,
      descriptionErr: null,
      contentErr: null,
      titleMsg: "",
      descriptionMsg: "",
      contentMsg: "",
      edit: false,
      articleError: false,
      updateError: false,
      deleteError: false,
    };
  },
  mounted() {
    axios
      .get(`/api/article/${this.$route.params.slug}/`)
      .then((response) => {
        this.article = response.data;
        this.title = this.article.title;
        this.description = this.article.description;
        this.content = this.article.content;
        this.setPermission();
      })
      .catch((error) => {
        this.articleError = true;
      });
  },
  methods: {
    setPermission() {
      axios
        .get("/api/auth/users/me/")
        .then((response) => {
          if (this.article.author === response.data.username) {
            this.canEdit = true;
          } else {
            this.canEdit = false;
          }
        })
        .catch((error) => {
          this.canEdit = false;
        });
    },
    setInputEvent() {
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
    changeEdit() {
      this.edit = !this.edit;
      if (this.edit) {
        setTimeout(this.setInputEvent, 500);
      }
    },
    updateArticle() {
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
        // set values
        let article = this.article;
        article.title = this.title;
        article.description = this.description;
        article.content = this.content;
        // send data
        axios
          .put(`/api/article/${this.$route.params.slug}/`, article)
          .then((response) => {
            // change page
            this.edit = false;
            this.$router.push(`/article/${article.slug}`);
          })
          .catch((error) => {
            this.updateError = true;
          });
      }
    },
    removeArticle() {
      axios
        .delete(`/api/article/${this.$route.params.slug}/`)
        .then((response) => {
          this.$router.push(`/`);
        })
        .catch((error) => {
          this.deleteError = true;
        });
    },
  },
};
</script>

<style>
@import "../assets/form.css";
.btn-icon {
  margin-right: 3px;
  margin-bottom: 2px;
  width: 15px;
  height: 15px;
}
</style>
