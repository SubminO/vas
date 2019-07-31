<template>
  <b-modal
    ref="modal"
    :id="name"
    @hidden="handleHide"
    @ok="handleOk"
  >
    <template v-if="!title" slot="modal-header">&nbsp;</template>
    <template v-if="title" slot="modal-title">{{ title }}</template>

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
        default: null,
      },
      name: {
        type: String,
        required: true,
      }
    },
    methods: {
      handleHide: () => eventBus.$emit('modal-hidden'),
      handleOk: () => eventBus.$emit('modal-ok'),
    }
  }
</script>