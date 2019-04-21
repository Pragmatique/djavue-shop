// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import store from './store'
import CreateProduct from './components/CreateProduct.vue'
import Home from './components/Home.vue'
import ProductsInOrderList from './components/ProductsInOrderList'

Vue.config.productionTip = false

Vue.use(VueRouter)
// Define routes
const routes = [
  { path: '/productList', component: ProductsInOrderList },
  { path: '/makePurchase', component: CreateProduct },
  { path: '/home', component: ProductsInOrderList }
]
// Register routes
const router = new VueRouter({
  mode: 'history',
  routes
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  template: '<App/>',
  components: {App, Home, CreateProduct},
  router: router
})
