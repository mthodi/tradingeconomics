import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'

import 'material-design-icons/iconfont/material-icons.css'
import 'typeface-roboto/index.css'

Vue.use(require('vue-moment'));
Vue.use(Vuetify);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
