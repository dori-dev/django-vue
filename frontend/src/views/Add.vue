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
      <form @submit.prevent="createArticle">
        <div class="inputs mb-4">
          <div class="group mb-3">
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
          <div class="group mb-3">
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
          <div class="group">
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
        <button class="btn btn-primary w-75 mt-3">Create Article</button>
      </form>
    </div>
  </div>
</template>

<script>
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
    createArticle() {
      const genSlug = (length) => {
        let result = "";
        const characters =
          "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        const charactersLength = characters.length;
        let counter = 0;
        while (counter < length) {
          result += characters.charAt(
            Math.floor(Math.random() * charactersLength)
          );
          counter += 1;
        }
        return result;
      };
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
      let article = {
        title: this.title,
        slug: genSlug(8),
        description: this.description,
        content: this.content,
        author: "salar",
      };
      let articles = localStorage.getItem("articles");
      articles = JSON.parse(articles);
      articles.push(article);
      let db = JSON.stringify(articles);
      localStorage.setItem("articles", db);
      this.$router.push(`/article/${article.slug}`);
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
.input {
  display: block;
  border: 1px solid rgb(228, 228, 228);
  font-size: 16px;
  width: 100%;
  padding: 0 15px;
  margin-bottom: 10px;
  z-index: 2 !important;
  background-color: transparent !important;
  outline: none;
  border-radius: 5px;
  position: relative !important;
  transition: border-color 0.3s;
}
.input:focus {
  border: 2px solid #1a73e8 !important;
  box-shadow: none !important;
}
textarea {
  resize: none !important;
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
input[type="text"]:focus ~ .input-label {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
input[type="text"]:target ~ .input-label {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
textarea:focus ~ .input-label {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
}
textarea:target ~ .input-label {
  top: -7px;
  color: #1864c9;
  font-size: 13px;
  background-color: rgb(255, 255, 255);
  z-index: 2;
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
