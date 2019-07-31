import Vue from 'vue';
import Router from 'vue-router';

import { BASE_URL } from "./constants";

import HomePage    from './views/Home/Home';
import RouteEditor from './views/RouteEditor/RouteEditor';
import Http404     from './components/BaseErrors/Http404';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: BASE_URL,
  routes: [
    {
      path: '/',
      name: 'root',
      component: HomePage,
      meta: {
        title: 'Welcome to VAS',
      }
    },
    {
      path: '/routes',
      name: 'routes',
      component: RouteEditor,
      meta: {
        title: 'Route editor'
      }
    },
    {
      path: '*',
      name: 'http404',
      component: Http404,
    }
  ],
});

