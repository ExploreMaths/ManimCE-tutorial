<script setup lang="ts">
import { onMounted, ref } from 'vue'

const isDark = ref(false)

function apply(dark: boolean) {
  isDark.value = dark
  document.documentElement.dataset.theme = dark ? 'dark' : 'light'
  try {
    localStorage.setItem('mce-theme', dark ? 'dark' : 'light')
  } catch {
    // localStorage 不可用时忽略
  }
}

function toggle() {
  apply(!isDark.value)
}

onMounted(() => {
  let saved: string | null = null
  try {
    saved = localStorage.getItem('mce-theme')
  } catch {
    saved = null
  }
  if (saved === 'dark' || saved === 'light') {
    apply(saved === 'dark')
  } else {
    apply(window.matchMedia('(prefers-color-scheme: dark)').matches)
  }
})
</script>

<template>
  <button type="button" class="theme-toggle" :aria-label="'切换主题'" @click="toggle">
    <svg v-if="isDark" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
    </svg>
    <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <circle cx="12" cy="12" r="4"></circle>
      <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"></path>
    </svg>
  </button>
</template>

<style scoped>
.theme-toggle {
  display: inline-flex;
  flex: 0 0 32px;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  background: transparent;
  color: var(--text, #222);
  cursor: pointer;
}
.theme-toggle:hover {
  color: var(--accent, #2563eb);
  border-color: var(--accent, #2563eb);
}
</style>
