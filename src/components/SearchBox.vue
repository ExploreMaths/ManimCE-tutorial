<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import type { SearchItem } from '../types'

const router = useRouter()
const query = ref('')
const items = ref<SearchItem[]>([])
const indexLoaded = ref(false)
const indexLoading = ref(false)
const open = ref(false)
const activeIndex = ref(0)
const boxEl = ref<HTMLElement | null>(null)

const KIND_LABEL: Record<SearchItem['kind'], string> = {
  class: '类',
  function: '函数',
  section: '章节',
  glossary: '词汇',
}

const results = computed<SearchItem[]>(() => {
  const q = query.value.trim().toLowerCase()
  if (!q) return []
  return items.value
    .filter((it) => it.name.toLowerCase().includes(q))
    .slice(0, 12)
})

async function loadIndex() {
  if (indexLoaded.value || indexLoading.value) return
  indexLoading.value = true
  try {
    const res = await fetch(`${import.meta.env.BASE_URL}data/search-index.json`)
    if (res.ok) {
      const data = await res.json()
      if (Array.isArray(data)) items.value = data as SearchItem[]
    }
  } catch {
    // 索引加载失败时静默降级
  } finally {
    indexLoaded.value = true
    indexLoading.value = false
  }
}

function onFocus() {
  loadIndex()
  if (query.value.trim()) open.value = true
}

function onInput() {
  activeIndex.value = 0
  open.value = true
}

function close() {
  open.value = false
  activeIndex.value = 0
}

function go(item: SearchItem) {
  close()
  query.value = ''
  router.push(item.path)
}

function onKeydown(e: KeyboardEvent) {
  if (!open.value || !results.value.length) {
    if (e.key === 'Escape') close()
    return
  }
  if (e.key === 'ArrowDown') {
    e.preventDefault()
    activeIndex.value = (activeIndex.value + 1) % results.value.length
  } else if (e.key === 'ArrowUp') {
    e.preventDefault()
    activeIndex.value = (activeIndex.value - 1 + results.value.length) % results.value.length
  } else if (e.key === 'Enter') {
    e.preventDefault()
    go(results.value[activeIndex.value])
  } else if (e.key === 'Escape') {
    close()
  }
}

function onClickAway(e: MouseEvent) {
  if (boxEl.value && !boxEl.value.contains(e.target as Node)) {
    close()
  }
}

onMounted(() => document.addEventListener('click', onClickAway))
onBeforeUnmount(() => document.removeEventListener('click', onClickAway))
</script>

<template>
  <div ref="boxEl" class="search-box">
    <input
      v-model="query"
      type="search"
      aria-label="搜索类 / 函数 / 章节"
      placeholder="搜索类 / 函数 / 章节"
      @focus="onFocus"
      @input="onInput"
      @keydown="onKeydown"
    />
    <div v-if="open && query.trim()" class="search-dropdown" role="listbox">
      <button
        v-for="(item, i) in results"
        :key="item.path + item.name"
        type="button"
        class="search-item"
        :class="{ active: i === activeIndex }"
        @mouseenter="activeIndex = i"
        @click="go(item)"
      >
        <span class="search-name">{{ item.name }}</span>
        <span class="search-kind">{{ KIND_LABEL[item.kind] }}</span>
      </button>
      <div v-if="!results.length" class="search-empty">无结果</div>
    </div>
  </div>
</template>

<style scoped>
.search-box {
  position: relative;
}
.search-box input {
  width: 100%;
  padding: 0.35rem 0.7rem;
  font-size: 0.85rem;
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  background: var(--surface, #fff);
  color: var(--text, #222);
}
.search-dropdown {
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  right: 0;
  z-index: 50;
  max-height: 320px;
  overflow-y: auto;
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  background: var(--surface, #fff);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}
.search-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  width: 100%;
  padding: 0.4rem 0.7rem;
  font-size: 0.85rem;
  text-align: left;
  border: none;
  background: transparent;
  color: var(--text, #222);
  cursor: pointer;
}
.search-item.active {
  background: var(--bg, #f0f0f0);
}
.search-name {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.search-kind {
  flex-shrink: 0;
  font-size: 0.7rem;
  color: var(--muted, #888);
  border: 1px solid var(--border, #ddd);
  border-radius: 4px;
  padding: 0 0.35rem;
}
.search-empty {
  padding: 0.6rem 0.7rem;
  font-size: 0.85rem;
  color: var(--muted, #888);
}
</style>
