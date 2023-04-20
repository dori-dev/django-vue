<template>
  <nav class="navbar-primary">
    <a class="btn-expand-collapse">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
        <path
          d="M9.375 233.4l128-128c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L109.3 224H480c17.69 0 32 14.31 32 32s-14.31 32-32 32H109.3l73.38 73.38c12.5 12.5 12.5 32.75 0 45.25c-12.49 12.49-32.74 12.51-45.25 0l-128-128C-3.125 266.1-3.125 245.9 9.375 233.4z"
        />
      </svg>
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
        <router-link to="/profile">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <path
              d="M256 288c79.53 0 144-64.47 144-144s-64.47-144-144-144c-79.52 0-144 64.47-144 144S176.5 288 256 288zM351.1 320H160c-88.36 0-160 71.63-160 160c0 17.67 14.33 32 31.1 32H480c17.67 0 31.1-14.33 31.1-32C512 391.6 440.4 320 351.1 320z"
            />
          </svg>
          <span class="nav-label">Profile</span>
        </router-link>
      </li>
    </ul>
  </nav>
  <router-view class="main-content" />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
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
.main-content {
  margin-top: 60px;
  margin-left: 200px;
  padding: 20px;
}
.collapsed + .main-content {
  margin-left: 60px;
}
</style>
