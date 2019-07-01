import Router from 'vue-router'
import Vue from 'vue'

//views
import Home from './views/Home.vue'
import IndexDetails from './views/IndexDetails.vue'
import About from './views/About.vue'


Vue.use(Router)

const router = new Router({
    //mode : 'history',
    routes: [{
    
        path: '/',
        component : Home
    },{
        path: '/index/:symbol',
        component: IndexDetails,
        props : (route) => ({ query: route.query.symbol })
    },{
        path: '/about',
        component: About
    }]
})

export default router;