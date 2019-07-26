<template>
  <b-modal
    id="baseModal"
    ref="modal"
    :title="title"
    @hidden="handleHide"
    @ok="handleOk"
  >
    <template slot="modal-title">{{ title }}</template>

    <slot></slot>
  </b-modal>
</template>

<script>
  import { eventBus } from '../../eventBus'

  export default {
    name: 'BaseModal',
    props: {
      title: {
        type: String,
        required: true
      }
    },
    methods: {
      handleHide: () => eventBus.$emit('modal-hidden'),
      handleOk: () => eventBus.$emit('modal-ok'),
    }
  }
</script>