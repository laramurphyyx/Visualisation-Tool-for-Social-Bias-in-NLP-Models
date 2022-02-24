<template>
  <v-app>
    <v-app-bar app color="primary" flat>
      <v-app-bar-nav-icon class="white--text"></v-app-bar-nav-icon>
      <v-toolbar-title class="white--text">Based</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
