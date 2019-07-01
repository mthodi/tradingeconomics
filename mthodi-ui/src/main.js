import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'

import vueNumeralFilterInstaller from 'vue-numeral-filter';
import numeral from 'numeral';

Vue.use(require('vue-moment'));

Vue.use(vueNumeralFilterInstaller, {
  locale: 'en-gb'
});
Vue.use(numeral);
Vue.use(Vuetify);



Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
