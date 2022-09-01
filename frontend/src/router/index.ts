import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Post from '../views/Post.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import User from '../views/UserViews/User.vue';

import { useCookies } from 'vue3-cookies'
import { useStore } from '../store/store'

const {cookies}  = useCookies();
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: Post
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/user',
      name: 'user',
      component: User,
    }
  ]
})

router.beforeEach((to, from) => {
  if(to.matched.some(record => record.meta.hideForAuth)) {
    if(JSON.parse(cookies.get('loggedIn'))) {
      return {path: '/'}
    }
  }
})

export default router
