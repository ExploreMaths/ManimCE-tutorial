<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import type { DemoBlockData } from '../types'
import CodeBlock from './CodeBlock.vue'

const props = defineProps<{ demo: DemoBlockData }>()

const videoEl = ref<HTMLVideoElement | null>(null)
const areaEl = ref<HTMLDivElement | null>(null)
const shouldLoad = ref(false)
const baseUrl = import.meta.env.BASE_URL
let observer: IntersectionObserver | null = null
let copied = ref(false)
let copyTimer: ReturnType<typeof setTimeout> | null = null

function onIntersect(entries: IntersectionObserverEntry[]) {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      shouldLoad.value = true
      observer?.disconnect()
      observer = null
      break
    }
  }
}

onMounted(() => {
  // Observe the container, not the video: the <video> starts display:none
  // (v-show) and a hidden target never reports intersecting — deadlock.
  if (props.demo.video && areaEl.value) {
    observer = new IntersectionObserver(onIntersect, { rootMargin: '600px' })
    observer.observe(areaEl.value)
  }
})

onBeforeUnmount(() => {
  observer?.disconnect()
  if (copyTimer) clearTimeout(copyTimer)
})

async function copyCode() {
  try {
    await navigator.clipboard.writeText(props.demo.code)
    copied.value = true
    if (copyTimer) clearTimeout(copyTimer)
    copyTimer = setTimeout(() => (copied.value = false), 1500)
  } catch {
    // 剪贴板不可用时忽略
  }
}
</script>

<template>
  <div class="card demo-player">
    <div ref="areaEl" class="demo-video-area">
      <template v-if="demo.video">
        <video
          v-show="shouldLoad"
          ref="videoEl"
          controls
          loop
          muted
          playsinline
          preload="none"
          :src="shouldLoad ? baseUrl + demo.video : undefined"
        ></video>
        <div v-if="!shouldLoad" class="demo-placeholder">动画加载中…</div>
      </template>
      <div v-else class="demo-placeholder">视频渲染中（CI 自动生成）</div>
    </div>
    <div v-if="demo.caption" class="demo-caption" v-html="demo.caption"></div>
    <div class="demo-path">{{ demo.example }}.py</div>
    <details class="demo-source">
      <summary>查看源码</summary>
      <div class="demo-code">
        <button type="button" class="demo-copy" @click="copyCode">{{ copied ? '已复制' : '复制' }}</button>
        <CodeBlock :code="demo.code" lang="python" />
      </div>
    </details>
  </div>
</template>

<style scoped>
.demo-player {
  padding: 1rem;
  margin: 1rem 0;
}
.demo-video-area {
  position: relative;
  border-radius: 6px;
  background: var(--bg, #000);
}
.demo-video-area video {
  display: block;
  width: 100%;
  border-radius: 6px;
}
.demo-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 160px;
  color: var(--muted, #888);
  font-size: 0.85rem;
}
.demo-caption {
  margin-top: 0.6rem;
  font-size: 0.85rem;
  color: var(--muted, #888);
  line-height: 1.7;
}
.demo-path {
  margin-top: 0.4rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  color: var(--muted, #888);
}
.demo-source {
  margin-top: 0.5rem;
  font-size: 0.85rem;
}
.demo-source summary {
  cursor: pointer;
  color: var(--accent, #2563eb);
}
.demo-code {
  position: relative;
  margin-top: 0.5rem;
}
.demo-copy {
  position: absolute;
  top: 0.4rem;
  right: 0.4rem;
  z-index: 1;
  font-size: 0.72rem;
  padding: 0.15rem 0.55rem;
  border: 1px solid var(--border, #ddd);
  border-radius: 4px;
  background: var(--surface, #fff);
  color: var(--muted, #888);
  cursor: pointer;
}
.demo-copy:hover {
  color: var(--accent, #2563eb);
  border-color: var(--accent, #2563eb);
}
</style>
