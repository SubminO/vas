<template>
  <b-navbar
    :type="type"
    :variant="variant"
    :fixed="fixed"
    :sticky="sticky"
  >
    <b-navbar-brand
      :to="brandLink"
    >
      {{ brandContent }}
    </b-navbar-brand>

    <b-navbar-nav>
      <b-nav-item-dropdown text="Chapters">
        <b-dropdown-item
          v-for="ep in routesList"
          :disabled="ep.path === $root.cr"
          :href="ep.path"
          v-bind:key="ep.path"
        >
          {{ ep.meta.title }}
        </b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
  // https://bootstrap-vue.js.org/docs/components/navbar
  import { APP_NAME } from '../../constants';
  // import { routes } from '../../routes';

  export default {
    name: 'VNavBar',
    props: {
      variant: {
        type: String,
        default: 'info' // standard Bootstrap4 variants
      },
      type: {
        type: String,
        default: 'dark', // darl | lightt
      },
      fixed: {
        type: String,
        default: null
      },
      sticky: {
        type: Boolean,
        default: false
      },
      brandLink: {
        type: String,
        default: '/'
      },
      brandContent: {
        type: String,
        default: APP_NAME
      }
    },
    computed: {
      routesList() {
        return this.$router.options.routes.filter(
          i => (
            i.hasOwnProperty('path')
            && i.hasOwnProperty('meta')
            && i.meta.hasOwnProperty('title')
          )
        );
      },
    }
  }
</script>

<style>
</style>