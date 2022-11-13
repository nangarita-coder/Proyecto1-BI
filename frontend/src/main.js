import { createApp } from 'vue'
import App from './App.vue'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const myV3App = createApp(App)
.use(ElementPlus)

myV3App.mount('#app')