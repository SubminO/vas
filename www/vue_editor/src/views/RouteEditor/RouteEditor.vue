<template>
  <div id="routes">
    <items-table
      title="Route list"
      :items="items"
      :fields="fields"
      :isBusy="isBusy"
    />
    <modal name="formModal" :title="modalTitle">
      <editor-form :current-route="current"/>
    </modal>
    <modal name="deleteConfirmModal">
      <h6>Do you really want to delete the route '{{ current.name }}'?</h6>
    </modal>
  </div>
</template>

<script>
  import {
    EMPTY_ROUTE,
    RETRIEVE_INTERVAL
  } from '../../constants';

  import { eventBus } from '../../eventBus';

  import ItemsTable from '../../components/BaseTable/BaseTable';
  import EditorForm from '../RouteEditorForm/RouteEditorForm';
  import Modal from '../../components/BaseModal/BaseModal';

  export default {
    name: 'RouteEditor',
    components: {
      ItemsTable,
      Modal,
      EditorForm,
    },
    data() {
      return {
        handler: null,
        isBusy: false,
        current: {},
        items: [],
        fields: [
          {key: 'name', label: 'Name', sortable: true},
          {key: 'description', label: 'Description'},
          {key: 'platforms', label: 'Platforms'},
          {key: 'actions', label: ''},
        ],

      }
    },
    async created () {
      const that = this;

      eventBus.$on('item-select', function (item) {
        that.current = item;
        that.handler = that.updateRoute;
        that.showModal('formModal');
      });
      eventBus.$on('item-create', function () {
        that.current = EMPTY_ROUTE;
        that.handler = that.createRoute;
        that.showModal('formModal');
      });
      eventBus.$on('item-delete', async function(item) {
        that.current = item;
        that.handler = that.deleteRoute;
        that.showModal('deleteConfirmModal');
      });
      eventBus.$on('modal-ok', async function() {
        await that.handler();
        that.current = EMPTY_ROUTE;
      });
      eventBus.$on('modal-hidden', async function() {
        that.current = EMPTY_ROUTE;
      });
      eventBus.$on('system-busy', function () {
        that.isBusy = true
      });
      eventBus.$on('system-idle', function () {
        that.isBusy = false
      });
    },
    async mounted () {
      // await this.retrieveRoutes();

      this.interval = setInterval(function () {
        this.retrieveRoutes();
      }.bind(this), RETRIEVE_INTERVAL);
    },
    computed: {
      modalTitle () {
        return (
          Object.entries(this.current).length > 0
          && this.current.hasOwnProperty('name')
          && this.current.name.length > 0
        )
          ? `Edit route '${this.current.name}'`
          : 'Create new route';
      }
    },
    methods: {
      showModal (modal) {
        this.$bvModal.show(modal);
      },
      async retrieveRoutes ()  {
        if ( this.isBusy === true ) return;

        try {
          this.items = await this.$api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        }
      },
      async deleteRoute () {
        if ( this.isBusy === true ) return;
        eventBus.$emit('system-busy');

        try {
          await this.$api.delete(`/api/routes/${this.current.id}/`);
          this.items = await this.$api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        }

        eventBus.$emit('system-idle');
      },
      async createRoute () {
        if ( this.isBusy === true ) return;
        eventBus.$emit('system-busy');

        try {
          await this.$api.create('/api/routes/', null, this.current);
          this.items = await this.$api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        }

        eventBus.$emit('system-idle');
      },
      async updateRoute () {
        if ( this.isBusy === true ) return;
        eventBus.$emit('system-busy');

        try {
          await this.$api.update(`/api/routes/${this.current.id}/`, null, this.current);
          this.items = await this.$api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        }

        eventBus.$emit('system-idle');
      }

    }
  }
</script>

<style>
</style>
