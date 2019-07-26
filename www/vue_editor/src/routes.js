import HomePage    from './components/Home/Home';
import RouteEditor from './components/RouteEditor/RouteEditor';
import Http404     from './components/BaseErrors/Http404';

export const routes = [
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
];
