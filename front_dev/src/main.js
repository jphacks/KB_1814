// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui' // 追記
import locale from 'element-ui/lib/locale/lang/ja' // 追記
import 'element-ui/lib/theme-chalk/index.css' // 追記
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.config.productionTip = false
Vue.use(ElementUI, {locale})

Vue.use(VueGoogleMaps, {
  load: {
    // Google API key
    apiKey: 'AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8',
    // Enable more Google Maps libraries here
    libraries: ['places'],
    // Use new renderer
    useBetaRenderer: false,
  },
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
