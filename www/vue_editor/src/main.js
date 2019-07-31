import Vue from 'vue'
import Bootstrap from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import api from './api';
import router from './router';
import App from './layouts/Main';

Vue.config.productionTip = false;
Vue.prototype.$api = api;

Vue.use(Bootstrap);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
