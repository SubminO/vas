<template>
  <main-layout>
    <items-table
      title="Route list"
      :items="items"
      :fields="fields"
    />
    <modal :title="modalTitle">
      <editor-form :current-route="current"/>
    </modal>
  </main-layout>
</template>

<script>
  import { EMPTY_ROUTE } from '../../constants';
  import { eventBus } from '../../eventBus';

  import MainLayout from '../../layouts/Main';
  import ItemsTable from '../BaseTable/BaseTable';
  import EditorForm from '../RouteEditorForm/RouteEditorForm';
  import Modal from '../BaseModal/BaseModal';

  export default {
    name: 'RouteEditor',
    components: {
      MainLayout,
      ItemsTable,
      Modal,
      EditorForm,
    },
    data() {
      return {
        handler: null,
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
        Object.assign(that.current, item);
        that.handler = that.updateRoute;
        that.showModal();
      });
      eventBus.$on('item-create', function () {
        Object.assign(that.current, EMPTY_ROUTE);
        that.handler = that.createRoute;
        that.showModal();
      });
      eventBus.$on('item-delete', async function(item) {
        Object.assign(that.current, item);
        await that.deleteRoute();
      });
      eventBus.$on('modal-ok', async function() {
        await that.handler();
        Object.assign(that.current, EMPTY_ROUTE);
      });
      eventBus.$on('modal-hidden', async function() {
        Object.assign(that.current, EMPTY_ROUTE);
      });

      // Eventlisteners  настроены, можно получить внешние даггые
      await that.retrieveRoutes();
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
      showModal () {
        this.$bvModal.show('baseModal');
      },
      async retrieveRoutes ()  {
        try {
          eventBus.$emit('system-busy');
          this.items = await this.$root.api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        } finally {
          eventBus.$emit('system-unbusy');
        }
      },
      async deleteRoute () {
        try {
          eventBus.$emit('system-busy');
          await this.$root.api.delete(`/api/routes/${this.current.id}/`);
          this.items = await this.$root.api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        } finally {
          eventBus.$emit('system-unbusy');
        }
      },
      async createRoute () {
        try {
          eventBus.$emit('system-busy');
          await this.$root.api.create('/api/routes/', null, this.current);
          this.items = await this.$root.api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        } finally {
          eventBus.$emit('system-unbusy');
        }
      },
      async updateRoute () {
        try {
          eventBus.$emit('system-busy');
          await this.$root.api.update(`/api/routes/${this.current.id}/`, null, this.current);
          this.items = await this.$root.api.retrieve('/api/routes/');
        } catch (e) {
          // todo log error
          console.warn(e);
        } finally {
          eventBus.$emit('system-unbusy');
        }
      }

    }
  }
</script>

<style>
</style>
