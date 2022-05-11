import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Phishing from './views/Phishing.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'phishing',
      component: Phishing
    }
  ]
})
