import Home from './views/Home.vue'
import About from './views/About.vue'

export const routes = [
    {
        path: '/',
        component: Home,
        name: 'Home'
    },
    {
        path: '/about',
        component: About,
        name: 'About'
    },
    {
        path: '/todos',
       // component: Todos,
        name: 'Todos'
    }
]