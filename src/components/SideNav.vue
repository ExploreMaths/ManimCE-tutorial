<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import type { SiteNav } from '../types'

const props = defineProps<{ nav: SiteNav }>()
const emit = defineEmits<{ (e: 'close'): void }>()

const route = useRoute()
const STORAGE_KEY = 'mce-nav'

function loadExpanded(): Record<string, boolean> {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (raw) return JSON.parse(raw) as Record<string, boolean>
  } catch {
    // 忽略损坏的存储
  }
  return {}
}

const saved = loadExpanded()
const currentPart = computed(() => {
  for (const part of props.nav.parts) {
    if (part.sections.some((s) => s.path === route.path)) return part.id
  }
  return null
})

const expanded = ref<Record<string, boolean>>({})
for (const part of props.nav.parts) {
  expanded.value[part.id] = saved[part.id] ?? part.id === currentPart.value
}

watch(
  expanded,
  (val) => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(val))
    } catch {
      // 存储不可用时忽略
    }
  },
  { deep: true },
)

function toggle(partId: string) {
  expanded.value[partId] = !expanded.value[partId]
}

function isActive(path: string) {
  return path === route.path
}

function onSectionClick() {
  emit('close')
}
</script>

<template>
  <nav class="side-nav" aria-label="章节导航">
    <div v-for="part in nav.parts" :key="part.id" class="nav-part">
      <button
        type="button"
        class="nav-part-header"
        :aria-expanded="expanded[part.id]"
        @click="toggle(part.id)"
      >
        <span class="nav-part-title">{{ part.title }}</span>
        <span class="nav-part-count">{{ part.sections.length }} 节</span>
        <span class="nav-part-caret">{{ expanded[part.id] ? '▾' : '▸' }}</span>
      </button>
      <ul v-show="expanded[part.id]" class="nav-sections">
        <li v-for="section in part.sections" :key="section.id">
          <RouterLink
            class="nav-section-link"
            active-class="active"
            :to="section.path"
            :aria-current="isActive(section.path) ? 'page' : undefined"
            @click="onSectionClick"
          >
            {{ section.title }}
          </RouterLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.side-nav {
  font-size: 0.88rem;
}
.nav-part {
  margin-bottom: 0.25rem;
}
.nav-part-header {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  width: 100%;
  padding: 0.45rem 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  text-align: left;
  border: none;
  background: transparent;
  color: var(--text, #222);
  cursor: pointer;
  border-radius: 6px;
}
.nav-part-header:hover {
  background: var(--bg, #f0f0f0);
}
.nav-part-title {
  flex: 1;
}
.nav-part-count {
  font-size: 0.72rem;
  font-weight: 400;
  color: var(--muted, #888);
}
.nav-part-caret {
  font-size: 0.7rem;
  color: var(--muted, #888);
}
.nav-sections {
  list-style: none;
  margin: 0;
  padding: 0 0 0.25rem 0.75rem;
}
.nav-section-link {
  display: block;
  padding: 0.3rem 0.5rem;
  border-radius: 6px;
  color: var(--muted, #666);
  text-decoration: none;
  line-height: 1.5;
}
.nav-section-link:hover {
  color: var(--accent, #2563eb);
  background: var(--bg, #f0f0f0);
}
.nav-section-link.active {
  color: var(--accent, #2563eb);
  font-weight: 600;
}
</style>
