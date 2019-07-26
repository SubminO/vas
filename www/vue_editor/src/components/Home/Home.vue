<template>
  <main-layout>
    <p>Home page</p>
  </main-layout>
</template>

<script>
  import { eventBus } from '../../eventBus';

  import MainLayout from '../../layouts/Main';

  export default {
    name: 'HomePage',
    components: {
      MainLayout
    },
    created () {
      eventBus.$on('item-select', item => {
        console.log('@item-select fired in home', item)
      }),
        eventBus.$on('item-delete', item => {
          console.log('@item-delete fired in home', item)
        })
    }

  }
</script>

<style>

</style>