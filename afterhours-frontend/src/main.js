import Vue from 'vue';
import vuetify from '@/plugins/vuetify';
import axios from 'axios';
import App from '@/App.vue';

axios.defaults.baseURL = 'http://localhost:8000/';

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app');
