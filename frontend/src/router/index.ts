import { nextDay } from 'date-fns';
import { scroll } from 'quasar';
import { createRouter, createWebHistory } from 'vue-router'
import type {RouterScrollBehavior, RouteRecordRaw, Router, NavigationGuard} from 'vue-router' 
// import type { ScrollPositionNormalized }from 'vue-router'
// import Vue from 'vue'
import { useCookies } from 'vue3-cookies'
import { store } from '../store/store'
import { getParentRouterPath } from '@/assets/parentPath';

const { cookies }  = useCookies();

// type ScrollPositionNormalized = {
//   behavior?: ScrollOptions['behavior']
//   left: number
//   top: number
// }

// declare module 'vue-router' {
//   interface RouteMeta {
//     scrollPos?: ScrollPositionNormalized
//   }
// }

// const routes: RouteRecordRaw[] = [
//   {
//     path: '/search',
//     name: 'Search',
//     component: () => import('../views/Search.vue')
//   },
//   {
//     path: '/home',
//     name: 'Home',
//     component: () => import('../views/Home.vue'),
//     meta: {
//       auth: true
//     },
//   },
//   {
//     path: '/explore',
//     name: 'Explore',
//     component: () => import('../views/Explore.vue'),
//   },
//   {
//     path: '/login',
//     name: 'login',
//     component: () => import('../views/Login.vue'),
//     meta: {
//       hideForAuth: true
//     }
//   },
//   {
//     path: '/register',
//     name: 'register',
//     component: () => import('../views/Register.vue'),
//     meta: {
//       hideForAuth: true
//     }
//   },
//   {
//     path: '/settings',
//     name: 'settings',
//     component: () => import('@/views/Settings.vue'),
//     meta: {
//       auth: true
//     }
//   },
//   {
//     path: '/:username?',
//     name: 'user-profile',
//     component: () => import('../views/User.vue'),
//     // alias: '/:username?/user-posted',
//     redirect: {
//       name: 'user-posted'
//     },
//     children : [
//       {
//         path: '',
//         name: 'user-posted',
//         component: () => import('../components/UserProfile/UserPosted.vue'),
//       },
//       {
//         path: 'liked',
//         name: 'user-liked',
//         component: () => import('../components/UserProfile/UserLiked.vue'),
//       },
//     ],
//   },
//   {
//     path: '/:pathMatch(.*)*',
//     component: () => import('../views/PageNotFound.vue'),
//   }
// ]

// const scrollBehavior: RouterScrollBehavior = (to, from, savedPosition) => {
//   if (to.name === from.name) {
//     to.meta?.scrollPos && (to.meta.scrollPos.top = 0)
//     return { left: 0, top: 0 }
//   }
//   const scrollpos = savedPosition || to.meta?.scrollPos || { left: 0, top: 0 }
//   return new Promise((resolve, reject) => {
//     resolve(scrollpos)
//   })
// }


const router: Router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  
  routes: [
    {
      path: '/search',
      name: 'Search',
      // meta: {basePath: '/search'},
      component: () => import('../views/Search.vue')
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('../views/Home.vue'),
      meta: {
        auth: true
      },
    },
    {
      path: '/explore',
      name: 'Explore',
      component: () => import('../views/Explore.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/Register.vue'),
      meta: {
        hideForAuth: true
      }
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('@/views/Settings.vue'),
      meta: {
        auth: true
      }
    },
    {
      path: '/:username?',
      name: 'user-profile',
      component: () => import('../views/User.vue'),
      alias: '/:username?/*',
      // meta: {basePath: '/:username?'},
      redirect: {
        name: 'user-posted'
      },
      children : [
        {
          // path: getParentRouterPath(this), 
          path: '',
          alias: '*',
          name: 'user-posted',
          // meta: {basePath: getParentRouterPath(this)},
          component: () => import('../components/UserProfile/UserPosted.vue'),
        },
        {
          // path: getParentRouterPath(this) + '/likes',
          path: 'likes',
          alias: 'likes/*',
          name: 'user-liked',
          // meta: {basePath: getParentRouterPath(this) + '/likes'},
          component: () => import('../components/UserProfile/UserLiked.vue'),
        },
      ],
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('../views/PageNotFound.vue'),
    }
  ]
})

// router.beforeEach((to, from) => {
//   from.meta?.scrollPos && (from.meta.scrollPos.top = document.documentElement.scrollTop)
// })

router.beforeResolve((to, next) => {
  if(to.matched.some(record => record.meta.hideForAuth) && store.state.authenticated) {
    return {path: '/home'}
  }

  if(to.matched.some(record => record.meta.auth) && !store.state.authenticated) {
    return {path: '/login'}
  }
}) 

export default router
