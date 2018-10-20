import Vue from 'vue'
import Router from 'vue-router'

//import HelloWorld from '@/components/HelloWorld'
import Scene1 from '@/components/Scene1'
import Scene2 from '@/components/Scene2'
import axios from 'axios'

Vue.prototype.$axios = axios; // この行を追加

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Scene1',
      component: Scene1
    }
    , {
      path: '/Scene2',
      name: 'Scene2',
      component: Scene2
    }
   
  ]
})

