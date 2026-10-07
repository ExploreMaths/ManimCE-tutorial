<script setup lang="ts">
import { onMounted, ref } from 'vue'
import SideNav from '@/components/SideNav.vue'
import SearchBox from '@/components/SearchBox.vue'
import ThemeToggle from '@/components/ThemeToggle.vue'
import { loadNav, nav } from './store'

const drawerOpen = ref(false)

function openDrawer() {
  drawerOpen.value = true
}

function closeDrawer() {
  drawerOpen.value = false
}

onMounted(() => {
  loadNav().catch(() => {
    // 数据尚未生成（开发环境）时静默失败，界面显示骨架占位。
  })
})
</script>

<template>
  <div class="app-shell">
    <header class="site-header">
      <div class="header-inner">
        <button
          class="hamburger"
          type="button"
          aria-label="打开目录"
          @click="openDrawer"
        >
          <span></span><span></span><span></span>
        </button>
        <RouterLink to="/" class="site-title">ManimCE 教程</RouterLink>
        <div class="header-tools">
          <SearchBox />
          <ThemeToggle />
        </div>
      </div>
    </header>

    <div class="app-body">
      <aside class="sidebar">
        <SideNav v-if="nav" :nav="nav" />
        <div v-else class="nav-skeleton" aria-hidden="true">
          <div class="skeleton-line"></div>
          <div class="skeleton-line short"></div>
          <div class="skeleton-line"></div>
          <div class="skeleton-line short"></div>
          <div class="skeleton-line"></div>
        </div>
      </aside>

      <div v-if="drawerOpen" class="scrim" @click="closeDrawer"></div>
      <aside class="sidebar drawer" :class="{ open: drawerOpen }">
        <SideNav v-if="nav" :nav="nav" @close="closeDrawer" />
        <div v-else class="nav-skeleton" aria-hidden="true">
          <div class="skeleton-line"></div>
          <div class="skeleton-line short"></div>
          <div class="skeleton-line"></div>
        </div>
      </aside>

      <main class="main-content">
        <RouterView />
      </main>
    </div>

    <footer class="site-footer">
      <a href="https://github.com/ExploreMaths/ManimCE-tutorial" target="_blank" rel="noopener">
        ManimCE v0.21.0 · 源码托管于 GitHub · 动画由 CI 增量渲染
      </a>
    </footer>
  </div>
</template>
