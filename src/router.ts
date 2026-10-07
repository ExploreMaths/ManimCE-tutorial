import { createRouter, createWebHistory, type RouterScrollBehavior } from 'vue-router'
import { takeScrollRestore } from './composables/useProgress'

const scrollBehavior: RouterScrollBehavior = (to, _from, savedPosition) => {
  if (to.hash) {
    return { el: to.hash }
  }
  if (savedPosition) {
    return savedPosition
  }
  const y = takeScrollRestore(to.fullPath)
  if (y !== null) {
    return { top: y }
  }
  return { top: 0 }
}

export const router = createRouter({
  history: createWebHistory('/'),
  scrollBehavior,
  routes: [
    { path: '/', name: 'home', component: () => import('./views/HomeView.vue') },
    {
      path: '/ch/:part/:section',
      name: 'chapter',
      component: () => import('./views/ChapterView.vue')
    },
    { path: '/api', name: 'api', component: () => import('./views/ApiIndexView.vue') },
    { path: '/glossary', name: 'glossary', component: () => import('./views/GlossaryView.vue') },
    { path: '/:pathMatch(.*)*', name: 'not-found', component: () => import('./views/NotFoundView.vue') }
  ]
})
