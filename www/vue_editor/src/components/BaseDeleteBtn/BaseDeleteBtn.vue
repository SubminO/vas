<template>
  <div>
    <b-button
      :id="target"
      variant="outline-danger"
      @click="onClick"
    >
      <v-icon name="trash-alt"></v-icon>
    </b-button>
    <b-tooltip
      :target="target"
      :title="title"
      :placement="placement"
    ></b-tooltip>
  </div>
</template>

<script>
  import 'vue-awesome/icons/trash-alt';
  import VIcon from 'vue-awesome/components/Icon'

  import { eventBus } from '../../eventBus';

  export default {
    name: "DeleteBtn",
    components: {
      VIcon
    },
    props: {
      item: {
        type: Object,
        required: true
      },
      target: {
        type: String,
        required: true
      },
      title: {
        type: String,
        required: true
      },
      placement: {
        type: String,
        default: 'bottom'
      },
    },
    methods: {
      onClick (event) {
        event.preventDefault();
        eventBus.$emit('item-delete', this.item);
      }
    }
  };
</script>

<style scoped>

</style>