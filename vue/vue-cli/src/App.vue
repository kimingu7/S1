<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HeaderSection/>
    <MainContent/>
  </div>
</template>

<script>
import MainContent from './components/Main.vue'
import HeaderSection from './components/Header.vue'

export default {
  name: 'App',
  components: {
    HeaderSection,
    MainContent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
