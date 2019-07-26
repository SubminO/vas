import Vue from 'vue'

import VueRouter from 'vue-router';
Vue.use(VueRouter);

import { routes } from './routes';

const router = new VueRouter({
  routes
});

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import BootstrapVue from 'bootstrap-vue';
Vue.use(BootstrapVue);

import Api from './api/api';

Vue.config.productionTip = false;

const app = new Vue({
  router,
  data: {
    cr: window.location.pathname,
    api: Api,
  },
  computed: {
    ViewComponent () {
      let matchingRoute = routes.find(i => i.path === this.cr, this);
      matchingRoute = matchingRoute || routes.find(i => i.path === '*');
      return matchingRoute.component;
    },
  },
  render (h) {
    return h(this.ViewComponent)
  }
}).$mount('#app');

window.addEventListener('popstate', () => {
  app.cr = window.location.pathname
});
