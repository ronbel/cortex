import Home from './views/Home.vue'
import About from './views/About.vue'
import Users from './views/Users.vue'

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
        path: '/users',
        component: Users,
        name: 'Users'
    }
]