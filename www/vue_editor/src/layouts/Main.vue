<template>
  <b-container fluid>
    <v-nav-bar/>
    <slot></slot>
  </b-container>
</template>

<script>
  import VNavBar from '../components/BaseNavBar/BaseNavBar'

  export default {
    components: {
      VNavBar
    },
  }
</script>

<style scoped>
</style>
