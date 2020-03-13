import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import {routes} from './routes'

Vue.config.productionTip = false

const router = new VueRouter({routes, mode:'history'});


Vue.use(VueRouter)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
