<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { searchBase } from '../store'
import type { GlossaryItem } from '../types'

const items = ref<GlossaryItem[]>([])
const error = ref(false)
const loaded = ref(false)
const filter = ref('')

onMounted(() => {
  fetch(`${searchBase()}glossary.json`)
    .then((res) => {
      if (!res.ok) throw new Error(String(res.status))
      return res.json() as Promise<GlossaryItem[]>
    })
    .then((data) => {
      items.value = data
      loaded.value = true
    })
    .catch(() => {
      error.value = true
    })
})

const filtered = computed(() => {
  const q = filter.value.trim().toLowerCase()
  if (!q) return items.value
  return items.value.filter(
    (item) =>
      item.term.toLowerCase().includes(q) ||
      item.zh.includes(q) ||
      item.desc.toLowerCase().includes(q)
  )
})
</script>

<template>
  <div class="page-narrow" style="margin: 0 auto">
    <h1>术语表</h1>
    <p class="count-note">Manim 常见术语的中英文对照与说明。</p>

    <p v-if="error" class="state-box error">
      术语表数据加载失败，请确认内容已生成（运行 scripts/build_content.py）。
    </p>
    <p v-else-if="!loaded" class="state-box">术语表加载中……</p>

    <template v-else>
      <input
        v-model="filter"
        class="filter-input"
        type="search"
        placeholder="按术语 / 中文 / 说明过滤……"
        aria-label="过滤术语表"
      />
      <p class="count-note">
        共 {{ items.length }} 条<template v-if="filter">，匹配 {{ filtered.length }} 条</template>
      </p>

      <div v-if="filtered.length" class="table-wrap">
        <table class="data-table">
          <thead>
            <tr><th>术语</th><th>中文</th><th>说明</th></tr>
          </thead>
          <tbody>
            <tr v-for="item in filtered" :key="item.term">
              <td><code>{{ item.term }}</code></td>
              <td>{{ item.zh }}</td>
              <td>{{ item.desc }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p v-else class="state-box">没有匹配「{{ filter }}」的条目。</p>
    </template>
  </div>
</template>
