<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Breadcrumb from '@/components/Breadcrumb.vue'
import PrevNext from '@/components/PrevNext.vue'
import DemoPlayer from '@/components/DemoPlayer.vue'
import ParamTable from '@/components/ParamTable.vue'
import CompareTable from '@/components/CompareTable.vue'
import NoticeBox from '@/components/NoticeBox.vue'
import ExerciseBlock from '@/components/ExerciseBlock.vue'
import { searchBase } from '../store'
import { markVisited, saveScroll, takeScrollRestore } from '../composables/useProgress'
import type { Block, ChapterData } from '../types'

const route = useRoute()

const part = computed(() => String(route.params.part))
const section = computed(() => String(route.params.section))
const sectionPath = computed(() => `/ch/${part.value}/${section.value}`)

const data = ref<ChapterData | null>(null)
const error = ref(false)

const showToast = ref(false)
let toastTimer: number | undefined

function showToastOnce() {
  showToast.value = true
  toastTimer = window.setTimeout(() => {
    showToast.value = false
  }, 3000)
}

async function scrollToHash() {
  if (!route.hash) return
  await nextTick()
  const el = document.getElementById(route.hash.slice(1))
  if (el) {
    el.scrollIntoView({ block: 'start' })
  }
}

async function loadChapter() {
  data.value = null
  error.value = false
  const url = `${searchBase()}chapters/${part.value}/${section.value}.json`
  try {
    const res = await fetch(url)
    if (!res.ok) throw new Error(String(res.status))
    data.value = (await res.json()) as ChapterData
    document.title = `${data.value.title} · ${data.value.partTitle} · ManimCE 教程`
    markVisited(sectionPath.value)
    const y = takeScrollRestore(sectionPath.value)
    if (y !== null) {
      await nextTick()
      window.scrollTo(0, y)
      showToastOnce()
    } else {
      window.scrollTo(0, 0)
    }
    scrollToHash()
  } catch {
    error.value = true
    document.title = '章节加载失败 · ManimCE 教程'
  }
}

// 滚动保存（节流约 500ms）
let scrollTimer: number | undefined
let pendingY = 0

function onScroll() {
  pendingY = window.scrollY
  if (scrollTimer !== undefined) return
  scrollTimer = window.setTimeout(() => {
    scrollTimer = undefined
    saveScroll(sectionPath.value, pendingY)
  }, 500)
}

function onBeforeUnload() {
  saveScroll(sectionPath.value, window.scrollY)
}

const breadcrumbItems = computed(() => {
  const items: { label: string; to?: string }[] = [{ label: '首页', to: '/' }]
  if (data.value) {
    items.push({ label: data.value.partTitle })
    items.push({ label: data.value.title })
  }
  return items
})

function blockKey(block: Block, index: number): string {
  return `${block.type}-${index}`
}

onMounted(() => {
  loadChapter()
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('beforeunload', onBeforeUnload)
})

watch(() => [route.params.part, route.params.section], loadChapter)

onBeforeUnmount(() => {
  onBeforeUnload()
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('beforeunload', onBeforeUnload)
  if (scrollTimer !== undefined) window.clearTimeout(scrollTimer)
  if (toastTimer !== undefined) window.clearTimeout(toastTimer)
})
</script>

<template>
  <div class="content" style="margin: 0 auto">
    <p v-if="error" class="state-box error">
      章节内容加载失败。请确认内容已生成（运行 scripts/build_content.py），或返回
      <RouterLink to="/">首页</RouterLink>。
    </p>
    <p v-else-if="!data" class="state-box">章节加载中……</p>

    <template v-else>
      <Breadcrumb :items="breadcrumbItems" />
      <h1>{{ data.title }}</h1>

      <template v-for="(block, i) in data.blocks" :key="blockKey(block, i)">
        <h2 v-if="block.type === 'heading' && block.level === 2" :id="block.id">
          {{ block.text }}
          <a class="anchor" :href="`#${block.id}`" aria-label="锚点链接">#</a>
        </h2>
        <h3 v-else-if="block.type === 'heading' && block.level === 3" :id="block.id">
          {{ block.text }}
        </h3>
        <h4 v-else-if="block.type === 'heading'" :id="block.id">
          {{ block.text }}
        </h4>

        <div
          v-else-if="block.type === 'html'"
          class="html-block"
          v-html="block.html"
        ></div>

        <ParamTable v-else-if="block.type === 'params'" :rows="block.rows" />
        <CompareTable v-else-if="block.type === 'compare'" :headers="block.headers" :rows="block.rows" />
        <DemoPlayer v-else-if="block.type === 'demo'" :demo="block" />
        <NoticeBox
          v-else-if="block.type === 'notice'"
          :level="block.level"
          :title="block.title"
          :html="block.html"
        />
        <ExerciseBlock
          v-else-if="block.type === 'exercise'"
          :question-html="block.questionHtml"
          :answer-html="block.answerHtml"
        />

        <div v-else-if="block.type === 'inheritance'" class="chip-chain" aria-label="继承链">
          <template v-for="(name, j) in block.chain" :key="`${name}-${j}`">
            <span class="chip">{{ name }}</span>
            <span v-if="j < block.chain.length - 1" class="chip-sep" aria-hidden="true">›</span>
          </template>
        </div>
      </template>

      <p style="margin-top: 2rem">
        <RouterLink to="/">← 回到目录</RouterLink>
      </p>

      <PrevNext :prev="data.prev" :next="data.next" />
    </template>

    <div v-if="showToast" class="toast" role="status">已恢复到上次阅读处</div>
  </div>
</template>
