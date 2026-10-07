import { ref, watch } from 'vue'

export type Theme = 'dark' | 'light'

const STORAGE_KEY = 'mce-theme'
const theme = ref<Theme>(getInitialTheme())

function getInitialTheme(): Theme {
  const saved = localStorage.getItem(STORAGE_KEY)
  if (saved === 'dark' || saved === 'light') return saved
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

function applyTheme(value: Theme) {
  document.documentElement.dataset.theme = value
}

export function initTheme() {
  applyTheme(theme.value)
  watch(theme, (value) => {
    applyTheme(value)
    localStorage.setItem(STORAGE_KEY, value)
  })
}

export function useTheme() {
  function toggle() {
    theme.value = theme.value === 'dark' ? 'light' : 'dark'
  }
  return { theme, toggle }
}
