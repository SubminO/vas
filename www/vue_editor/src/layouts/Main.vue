<template>
  <div id="app">
    <b-container fluid>
      <nav-bar/>
      <router-view/>
    </b-container>
  </div>
</template>

<script>
  import NavBar from '../components/BaseNavBar/BaseNavBar'

  export default {
    components: {
      NavBar
    },
  }
</script>

<style scoped>
</style>
