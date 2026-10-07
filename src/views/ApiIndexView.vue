<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { searchBase } from '../store'
import type { ApiIndexGroup } from '../types'

const groups = ref<ApiIndexGroup[]>([])
const error = ref(false)
const loaded = ref(false)
const filter = ref('')

onMounted(() => {
  fetch(`${searchBase()}api-index.json`)
    .then((res) => {
      if (!res.ok) throw new Error(String(res.status))
      return res.json() as Promise<ApiIndexGroup[]>
    })
    .then((data) => {
      groups.value = data
      loaded.value = true
    })
    .catch(() => {
      error.value = true
    })
})

const totalCount = computed(() =>
  groups.value.reduce((sum, g) => sum + g.items.length, 0)
)

const filteredGroups = computed(() => {
  const q = filter.value.trim().toLowerCase()
  if (!q) return groups.value
  return groups.value
    .map((g) => ({
      letter: g.letter,
      items: g.items.filter((item) => item.name.toLowerCase().includes(q))
    }))
    .filter((g) => g.items.length > 0)
})

const filteredCount = computed(() =>
  filteredGroups.value.reduce((sum, g) => sum + g.items.length, 0)
)
</script>

<template>
  <div class="page-narrow" style="margin: 0 auto">
    <h1>API 速查索引</h1>
    <p class="count-note">按字母顺序浏览全部公共类与函数。</p>

    <p v-if="error" class="state-box error">
      索引数据加载失败，请确认内容已生成（运行 scripts/build_content.py）。
    </p>
    <p v-else-if="!loaded" class="state-box">索引加载中……</p>

    <template v-else>
      <input
        v-model="filter"
        class="filter-input"
        type="search"
        placeholder="按名称过滤……"
        aria-label="按名称过滤"
      />
      <p class="count-note">
        共 {{ totalCount }} 项<template v-if="filter">，匹配 {{ filteredCount }} 项</template>
      </p>

      <p v-if="filter && filteredCount === 0" class="state-box">没有匹配「{{ filter }}」的条目。</p>

      <section v-for="group in filteredGroups" :key="group.letter" class="api-letter-group">
        <h3>{{ group.letter }}</h3>
        <ul class="api-item-list">
          <li v-for="item in group.items" :key="item.name">
            <span class="badge" :class="`kind-${item.kind}`">{{ item.kind }}</span>
            <RouterLink :to="item.path">{{ item.name }}</RouterLink>
          </li>
        </ul>
      </section>
    </template>
  </div>
</template>
