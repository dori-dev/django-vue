<template>
  <nav class="navbar-primary collapsed">
    <a class="btn-expand-collapse">
      <div class="arrow-left" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
          <path
            d="M9.375 233.4l128-128c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L109.3 224H480c17.69 0 32 14.31 32 32s-14.31 32-32 32H109.3l73.38 73.38c12.5 12.5 12.5 32.75 0 45.25c-12.49 12.49-32.74 12.51-45.25 0l-128-128C-3.125 266.1-3.125 245.9 9.375 233.4z"
          />
        </svg>
      </div>
      <div class="arrow-right">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
          <path
            d="M502.6 278.6l-128 128c-12.51 12.51-32.76 12.49-45.25 0c-12.5-12.5-12.5-32.75 0-45.25L402.8 288H32C14.31 288 0 273.7 0 255.1S14.31 224 32 224h370.8l-73.38-73.38c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l128 128C515.1 245.9 515.1 266.1 502.6 278.6z"
          />
        </svg>
      </div>
    </a>
    <ul class="navbar-primary-menu pt-3">
      <li>
        <router-link to="/">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M575.1 256c-.0006 17.6-14.27 31.1-32.01 31.1L511.1 288l.0031 160c0 35.35-28.65 64-63.1 64H128c-35.35 0-63.1-28.65-63.1-64L64.02 288h-32.02c-17.78 0-32-14.44-32-31.1c-.0004-9.052 3.842-17.9 10.92-24.1l255.1-223.1c6.963-6.098 14.93-7.918 21.08-7.918c7.523 0 15.05 2.637 21.08 7.918l255.1 223.1C572.2 238.1 575.1 246.1 575.1 256z"
            />
          </svg>
          <span class="nav-label">Home</span>
        </router-link>
        <router-link to="/about">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
            <path
              d="M448 56v80C448 149.3 437.3 160 424 160S400 149.3 400 136V80h-152v352h48c13.25 0 24 10.75 24 24S309.3 480 296 480h-144C138.8 480 128 469.3 128 456s10.75-24 24-24h48v-352H48v56C48 149.3 37.25 160 24 160S0 149.3 0 136v-80C0 42.75 10.75 32 24 32h400C437.3 32 448 42.75 448 56z"
            />
          </svg>
          <span class="nav-label">About</span>
        </router-link>
        <router-link to="/profile" v-if="$store.state.isAuthenticated">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <path
              d="M256 288c79.53 0 144-64.47 144-144s-64.47-144-144-144c-79.52 0-144 64.47-144 144S176.5 288 256 288zM351.1 320H160c-88.36 0-160 71.63-160 160c0 17.67 14.33 32 31.1 32H480c17.67 0 31.1-14.33 31.1-32C512 391.6 440.4 320 351.1 320z"
            />
          </svg>
          <span class="nav-label">Profile</span>
        </router-link>
        <router-link to="/login" v-if="!$store.state.isAuthenticated">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <path
              d="M344.7 238.5l-144.1-136C193.7 95.97 183.4 94.17 174.6 97.95C165.8 101.8 160.1 110.4 160.1 120V192H32.02C14.33 192 0 206.3 0 224v64c0 17.68 14.33 32 32.02 32h128.1v72c0 9.578 5.707 18.25 14.51 22.05c8.803 3.781 19.03 1.984 26-4.594l144.1-136C354.3 264.4 354.3 247.6 344.7 238.5zM416 32h-64c-17.67 0-32 14.33-32 32s14.33 32 32 32h64c17.67 0 32 14.33 32 32v256c0 17.67-14.33 32-32 32h-64c-17.67 0-32 14.33-32 32s14.33 32 32 32h64c53.02 0 96-42.98 96-96V128C512 74.98 469 32 416 32z"
            />
          </svg>
          <span class="nav-label">Login</span>
        </router-link>
        <router-link to="/register" v-if="!$store.state.isAuthenticated">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
            <path
              d="M512 32H64C28.65 32 0 60.65 0 96v320c0 35.35 28.65 64 64 64h448c35.35 0 64-28.65 64-64V96C576 60.65 547.3 32 512 32zM176 128c35.35 0 64 28.65 64 64s-28.65 64-64 64s-64-28.65-64-64S140.7 128 176 128zM272 384h-192C71.16 384 64 376.8 64 368C64 323.8 99.82 288 144 288h64c44.18 0 80 35.82 80 80C288 376.8 280.8 384 272 384zM496 320h-128C359.2 320 352 312.8 352 304S359.2 288 368 288h128C504.8 288 512 295.2 512 304S504.8 320 496 320zM496 256h-128C359.2 256 352 248.8 352 240S359.2 224 368 224h128C504.8 224 512 231.2 512 240S504.8 256 496 256zM496 192h-128C359.2 192 352 184.8 352 176S359.2 160 368 160h128C504.8 160 512 167.2 512 176S504.8 192 496 192z"
            />
          </svg>
          <span class="nav-label">Register</span>
        </router-link>
        <router-link to="/logout" v-if="$store.state.isAuthenticated">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <path
              d="M256 288c17.67 0 32-14.33 32-32V32c0-17.67-14.33-32-32-32S224 14.33 224 32v224C224 273.7 238.3 288 256 288zM403.7 66.81c-13.92-10.84-34.03-8.406-44.92 5.5c-10.89 13.94-8.438 34.03 5.484 44.94C407.3 150.9 432 201.5 432 256c0 97.03-78.95 176-176 176S80 353 80 256c0-54.53 24.69-105.1 67.72-138.8c13.92-10.91 16.38-31 5.484-44.94c-10.91-13.91-31-16.34-44.92-5.5C49.64 112.7 16 181.7 16 256c0 132.3 107.7 240 240 240s240-107.7 240-240C496 181.7 462.4 112.7 403.7 66.81z"
            />
          </svg>
          <span class="nav-label">Logout</span>
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  mounted() {
    let navbar = document.querySelector(".navbar-primary");
    let btn = document.querySelector(".btn-expand-collapse");
    let navbarOpen = localStorage.getItem("navbarOpen");
    const changeIcon = (open) => {
      if (open === 1) {
        btn.querySelector(".arrow-left").removeAttribute("hidden");
        btn.querySelector(".arrow-right").setAttribute("hidden", "");
      } else {
        btn.querySelector(".arrow-left").setAttribute("hidden", "");
        btn.querySelector(".arrow-right").removeAttribute("hidden");
      }
    };
    if (navbarOpen == 1) {
      navbar.classList.remove("collapsed");
      changeIcon(1);
    } else {
      navbar.classList.add("collapsed");
      changeIcon(0);
    }

    btn.onclick = function (e) {
      navbar.classList.toggle("collapsed");
      localStorage.removeItem("navbarOpen");
      if (navbar.classList.contains("collapsed")) {
        localStorage.setItem("navbarOpen", 0);
        changeIcon(0);
      } else {
        localStorage.setItem("navbarOpen", 1);
        changeIcon(1);
      }
    };
  },
};
</script>

<style>
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #42b983;
}
svg {
  width: 20px;
  height: 20px;
  fill: #fefefe;
}
a {
  text-decoration: none !important;
}
.navbar-primary {
  background-color: #333;
  bottom: 0px;
  left: 0px;
  position: fixed;
  top: 0;
  width: 200px;
  z-index: 8;
  overflow: hidden;
  -webkit-transition: all 0.1s ease-in-out;
  -moz-transition: all 0.1s ease-in-out;
  transition: all 0.1s ease-in-out;
}

.navbar-primary.collapsed {
  width: 60px;
}

.navbar-primary.collapsed svg {
  font-size: 22px;
}

.navbar-primary.collapsed .nav-label {
  display: none;
}
.btn-expand-collapse {
  position: absolute;
  display: block;
  left: 0px;
  bottom: 0;
  width: 100%;
  padding: 8px 0;
  border-top: solid 1px #666;
  color: grey;
  font-size: 20px;
  text-align: center;
}
.btn-expand-collapse:hover,
.btn-expand-collapse:focus {
  background-color: #222;
  color: white;
}
.btn-expand-collapse:active {
  background-color: #111;
}
.navbar-primary-menu,
.navbar-primary-menu li {
  margin: 0;
  padding: 0;
  list-style: none;
}
.navbar-primary-menu li a {
  display: flex;
  padding: 10px 18px;
  text-align: left;
  border-bottom: solid 1px #444;
  color: #ccc;
}
.navbar-primary-menu li a:hover {
  background-color: #000;
  text-decoration: none;
  color: white;
}
.navbar-primary-menu li a svg {
  margin-right: 6px;
}
.navbar-primary-menu li a:hover svg {
  color: orchid;
}
.collapsed + .main-content {
  margin-left: 60px;
}
</style>
