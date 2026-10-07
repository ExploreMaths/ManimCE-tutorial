<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import NoticeBox from '@/components/NoticeBox.vue'
import InheritanceGraph from '@/components/InheritanceGraph.vue'
import ProgressCard from '@/components/ProgressCard.vue'
import { nav, searchBase } from '../store'
import { percentOf, resetAll, visitedCount } from '../composables/useProgress'
import type { GlossaryItem, GraphNode } from '../types'

const firstSectionPath = computed(() => {
  const first = nav.value?.parts[0]?.sections[0]
  return first ? first.path : null
})

const percent = computed(() => percentOf(nav.value?.totalSections ?? 0))
const visited = computed(() => visitedCount())

const progressCleared = ref(false)

function handleReset() {
  resetAll()
  progressCleared.value = true
  setTimeout(() => {
    progressCleared.value = false
  }, 3000)
}

const versionPoints = `<ul>
<li>新增 <code>Typst</code> 与 <code>MathTypst</code>，支持 Typst 排版引擎渲染数学公式。</li>
<li><code>Code</code> 高亮颜色改为 Pygments 配色方案，更贴近主流编辑器风格。</li>
<li><code>convert_pixel_array</code> 行为变更，返回值与默认参数有所调整。</li>
<li>新增 <code>max_inflight_encoders</code> 配置，支持多路并行编码以加快渲染。</li>
<li>CLI 的 <code>-g</code> / <code>-i</code> 选项已弃用，请改用 <code>--save_gif</code> / <code>--save_pngs</code> 等新选项。</li>
</ul>`

const graphNodes = ref<GraphNode[] | null>(null)
const graphError = ref(false)

const glossaryItems = ref<GlossaryItem[]>([])
const glossaryError = ref(false)

onMounted(() => {
  fetch(`${searchBase()}inheritance.json`)
    .then((res) => {
      if (!res.ok) throw new Error(String(res.status))
      return res.json() as Promise<GraphNode[]>
    })
    .then((data) => {
      graphNodes.value = data
    })
    .catch(() => {
      graphError.value = true
    })

  fetch(`${searchBase()}glossary.json`)
    .then((res) => {
      if (!res.ok) throw new Error(String(res.status))
      return res.json() as Promise<GlossaryItem[]>
    })
    .then((data) => {
      glossaryItems.value = data.slice(0, 12)
    })
    .catch(() => {
      glossaryError.value = true
    })
})
</script>

<template>
  <div class="page-narrow" style="margin: 0 auto">
    <section class="hero">
      <h1>ManimCE v0.21.0 交互式教程</h1>
      <p class="subtitle">
        覆盖全部公共类与函数 · 每个示例配预渲染动画 · 继承关系图 · 学习进度跟踪
      </p>
      <div class="hero-actions">
        <RouterLink v-if="firstSectionPath" :to="firstSectionPath" class="btn primary">
          初学者路径
        </RouterLink>
        <RouterLink to="/api" class="btn">进阶者速查</RouterLink>
      </div>
    </section>

    <section class="home-section">
      <h2>学习进度</h2>
      <ProgressCard
        v-if="nav"
        :percent="percent"
        :visited="visited"
        :total="nav.totalSections"
        @reset="handleReset"
      />
      <p v-if="progressCleared" class="inline-message" role="status">已清除学习进度</p>
    </section>

    <section class="home-section">
      <h2>v0.21.0 版本要点</h2>
      <NoticeBox level="version" title="v0.21.0 更新内容" :html="versionPoints" />
    </section>

    <section class="home-section">
      <h2>继承关系图</h2>
      <InheritanceGraph v-if="graphNodes" :nodes="graphNodes" />
      <p v-else-if="graphError" class="state-box error">
        继承关系图数据加载失败，请确认内容已生成（运行 scripts/build_content.py）。
      </p>
      <p v-else class="state-box">继承关系图加载中……</p>
    </section>

    <section class="home-section">
      <h2>术语表摘要</h2>
      <template v-if="glossaryItems.length">
        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr><th>术语</th><th>中文</th><th>说明</th></tr>
            </thead>
            <tbody>
              <tr v-for="item in glossaryItems" :key="item.term">
                <td><code>{{ item.term }}</code></td>
                <td>{{ item.zh }}</td>
                <td>{{ item.desc }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <RouterLink to="/glossary">查看完整术语表 →</RouterLink>
      </template>
      <p v-else-if="glossaryError" class="state-box error">
        术语表数据加载失败，请确认内容已生成（运行 scripts/build_content.py）。
      </p>
      <p v-else class="state-box">术语表加载中……</p>
    </section>
  </div>
</template>
