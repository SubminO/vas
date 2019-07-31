<template>
  <b-table
    hover
    borderless
    head-variant="light"
    caption-top
    selectable
    select-mode="single"
    @row-selected="handleRowSelected"
    :items="items"
    :fields="fields"
    :busy="isBusy"
    show-empty
    empty-text="No data..."
    primary-key="id"
  >
    <div slot="table-busy" class="text-center text-danger my-2">
      <b-spinner class="align-middle"></b-spinner>
      <strong>Loading...</strong>
    </div>

    <template slot="table-caption">
      <b-row  align-h="between">
        <b-col>
          <h4 class="d-inline text-left">{{ title }}</h4>
        </b-col>
        <b-col cols="1">
          <b-button variant="primary" @click="handleCreate">
            <v-icon name="plus"></v-icon>
          </b-button>
        </b-col>
      </b-row>
    </template>

    <template slot="empty" slot-scope="scope">
      <h4>{{ scope.emptyText }}</h4>
    </template>

    <template slot="actions" slot-scope="row">
      <delete-btn
        :item="row.item"
        :target="'item-' + row.item.id"
        :title="'Delete ' + row.item.name"
        placement="left"
      ></delete-btn>
    </template>
  </b-table>
</template>

<script>
  import { eventBus } from '../../eventBus';

  import 'vue-awesome/icons/plus';
  import VIcon from 'vue-awesome/components/Icon'
  import DeleteBtn from '../BaseDeleteButton/BaseDeleteButton';

  export default {
    name: 'ItemsTable',
    components: {
      VIcon,
      DeleteBtn
    },
    props: {
      items: {
        type: Array,
        required: true
      },
      fields: {
        type: Array,
        required: true
      },
      title: {
        type: String,
        required: true
      },
      isBusy: {
        type: Boolean,
        required: true,
      }
    },
    methods: {
      handleRowSelected (item) {
        eventBus.$emit('item-select', item[0]);
      },
      handleCreate () {
        eventBus.$emit('item-create')
      }
    }
  }
</script>