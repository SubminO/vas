<template>
  <form ref="form" @submit.stop.prevent="handleSubmit">
    <b-form-group
      id="input-group-name"
      label="Route name:"
      label-for="input-name"
      invalid-feedback="Name is required"
    >
      <b-form-input
        id="input-name"
        v-model="currentRoute.name"
        required
        placeholder="Enter route name"
        autofocus
      ></b-form-input>
    </b-form-group>
    <b-form-group
      id="input-group-description"
      label="Route description:"
      label-for="input-description"
    >
      <b-form-textarea
        id="input-description"
        v-model="currentRoute.description"
        placeholder="You can enter route description here..."
        rows="3"
      ></b-form-textarea>
    </b-form-group>
  </form>
</template>

<script>
  export default {
    name: 'RouteForm',
    props: {
      currentRoute: {
        type: Object,
        required: true
      }
    },
  }
</script>