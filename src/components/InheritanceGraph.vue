<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import type { GraphNode } from '../types'

const props = defineProps<{ nodes: GraphNode[] }>()
const router = useRouter()

const container = ref<HTMLElement | null>(null)
const collapsed = ref<Set<string>>(new Set())
const filter = ref('')
const ready = ref(false)

let vizPromise: Promise<import('@viz-js/viz').Viz> | null = null
function viz() {
  if (!vizPromise) vizPromise = import('@viz-js/viz').then((m) => m.instance())
  return vizPromise
}

/* ---------- tree helpers (same semantics as before) ---------- */

const byName = computed(() => {
  const map = new Map<string, GraphNode>()
  for (const n of props.nodes) map.set(n.name, n)
  return map
})

const childrenOf = computed(() => {
  const map = new Map<string, GraphNode[]>()
  for (const n of props.nodes) {
    if (n.parent && byName.value.has(n.parent)) {
      const list = map.get(n.parent) ?? []
      list.push(n)
      map.set(n.parent, list)
    }
  }
  return map
})

const roots = computed(() =>
  props.nodes.filter((n) => !n.parent || !byName.value.has(n.parent)),
)

function hasChildren(name: string) {
  return (childrenOf.value.get(name) ?? []).length > 0
}

/** Names visible with the current collapse set (collapsed node itself
 *  stays visible; its whole subtree is hidden). */
const visible = computed(() => {
  const set = new Set<string>()
  const queue: string[] = roots.value.map((r) => r.name)
  while (queue.length) {
    const name = queue.shift()!
    if (set.has(name)) continue
    set.add(name)
    if (collapsed.value.has(name)) continue
    for (const child of childrenOf.value.get(name) ?? []) queue.push(child.name)
  }
  return set
})

const dimmed = computed(() => {
  const q = filter.value.trim().toLowerCase()
  if (!q) return new Set<string>()
  return new Set(
    props.nodes.filter((n) => !n.name.toLowerCase().includes(q)).map((n) => n.name),
  )
})

/* ---------- dot source ---------- */

function displayName(name: string) {
  return name.length > 22 ? name.slice(0, 21) + '…' : name
}

const dot = computed(() => {
  const L: string[] = [
    'digraph G {',
    '  graph [rankdir=LR, bgcolor="transparent", nodesep="0.3", ranksep="0.6", splines=spline];',
    '  node  [shape=box, style="rounded,filled", fontname="Helvetica,sans-serif", fontsize=11, height=0.34, color="#8b93a1", fillcolor="#f2f4f7", fontcolor="#1f2733"];',
    '  edge  [color="#a6adba", arrowsize=0.6, penwidth=1.1];',
  ]
  const q = filter.value.trim().toLowerCase()
  for (const name of visible.value) {
    const hit = !q || name.toLowerCase().includes(q)
    const pen = hit ? '#5b64d6' : '#8b93a1'
    const fill = hit ? '#eef0fd' : '#f2f4f7'
    L.push(`  "${name}" [label="${displayName(name)}", color="${pen}", fillcolor="${fill}"];`)
  }
  for (const n of props.nodes) {
    if (!n.parent) continue
    if (!visible.value.has(n.name) || !visible.value.has(n.parent)) continue
    L.push(`  "${n.name}" -> "${n.parent}";`)
  }
  L.push('}')
  return L.join('\n')
})

/* ---------- render + decorate ---------- */

const NS = 'http://www.w3.org/2000/svg'

function decorate(svg: SVGSVGElement) {
  svg.classList.add('graphviz-svg')
  for (const g of Array.from(svg.querySelectorAll('g.node'))) {
    const title = g.querySelector('title')
    const name = title?.textContent ?? ''
    if (!name) continue
    const node = byName.value.get(name)
    g.style.cursor = node?.link || hasChildren(name) ? 'pointer' : 'default'
    g.addEventListener('click', (e) => {
      e.stopPropagation()
      if (node?.link) router.push(node.link)
      else if (hasChildren(name)) toggle(name)
    })
    // dim filtered-out nodes
    if (dimmed.value.has(name)) {
      g.style.opacity = '0.25'
      const edgeSel = `g.edge:has(> title):has(title)`
      void edgeSel
    }
    if (!hasChildren(name)) continue
    // fold toggle badge at the node's top-right corner
    const shape = g.querySelector(':scope > path')
    let bx = 0
    let by = 0
    if (shape) {
      const bb = shape.getBBox()
      bx = bb.x + bb.width
      by = bb.y
    }
    const badge = document.createElementNS(NS, 'g')
    badge.setAttribute('class', 'fold-badge')
    badge.style.cursor = 'pointer'
    const c = document.createElementNS(NS, 'circle')
    c.setAttribute('cx', String(bx))
    c.setAttribute('cy', String(by))
    c.setAttribute('r', '7')
    c.setAttribute('fill', '#5b64d6')
    c.setAttribute('stroke', '#ffffff')
    c.setAttribute('stroke-width', '1.5')
    const t = document.createElementNS(NS, 'text')
    t.setAttribute('x', String(bx))
    t.setAttribute('y', String(by + 3.5))
    t.setAttribute('text-anchor', 'middle')
    t.setAttribute('font-size', '10')
    t.setAttribute('font-weight', '700')
    t.setAttribute('fill', '#ffffff')
    t.setAttribute('pointer-events', 'none')
    t.textContent = collapsed.value.has(name) ? '+' : '−'
    badge.appendChild(c)
    badge.appendChild(t)
    badge.addEventListener('click', (e) => {
      e.stopPropagation()
      toggle(name)
    })
    g.appendChild(badge)
  }
  // dim edges whose endpoints are dimmed
  for (const e of Array.from(svg.querySelectorAll('g.edge'))) {
    const t = e.querySelector('title')?.textContent ?? '' // "child -> parent"
    const [child, parent] = t.split('->').map((s) => s.trim())
    if (dimmed.value.has(child) || dimmed.value.has(parent)) e.style.opacity = '0.25'
  }
}

function toggle(name: string) {
  const next = new Set(collapsed.value)
  if (next.has(name)) next.delete(name)
  else next.add(name)
  collapsed.value = next
}

function expandAll() {
  collapsed.value = new Set()
}

function collapseAll() {
  collapsed.value = new Set(
    props.nodes.filter((n) => hasChildren(n.name)).map((n) => n.name),
  )
}

async function render() {
  if (!container.value) return
  const v = await viz()
  const svg = v.renderSVGElement(dot.value)
  container.value.replaceChildren(svg) // mount first: getBBox needs a rendered tree
  decorate(svg)
  ready.value = true
}

let timer: ReturnType<typeof setTimeout> | null = null
watch([collapsed, filter], () => {
  if (timer) clearTimeout(timer)
  timer = setTimeout(render, 60) // coalesce rapid toggles
})

onMounted(render)
</script>

<template>
  <div class="graph-wrap">
    <div class="graph-toolbar">
      <input
        v-model="filter"
        type="search"
        aria-label="筛选类名"
        placeholder="筛选类名"
        class="graph-filter"
      />
      <button type="button" @click="expandAll">展开全部</button>
      <button type="button" @click="collapseAll">折叠全部</button>
    </div>
    <div ref="container" class="graph-container" :class="{ ready }"></div>
    <p v-if="!ready" class="state-box">继承关系图加载中……</p>
  </div>
</template>

<style scoped>
.graph-wrap {
  margin-top: 0.5rem;
}
.graph-toolbar {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}
.graph-filter {
  flex: 1;
  min-width: 10rem;
  padding: 0.35rem 0.6rem;
  border: 1px solid var(--border);
  border-radius: 0.5rem;
  background: var(--bg);
  color: var(--text);
}
.graph-container {
  overflow-x: auto;
  border: 1px solid var(--border);
  border-radius: 0.75rem;
  background: var(--surface);
  padding: 0.5rem;
}
.graph-container :deep(.graphviz-svg) {
  /* natural size, no squashing; the container scrolls horizontally */
  width: auto;
  height: auto;
  max-width: none;
  display: block;
}
/* theme adaptation over graphviz inline attributes
   (rounded nodes are <path>, edge arrowheads are <polygon>) */
.graph-container :deep(g.node path) {
  stroke-width: 1.2;
}
[data-theme='dark'] .graph-container :deep(g.node path) {
  fill: #1b2027 !important;
  stroke: #39414d !important;
}
[data-theme='dark'] .graph-container :deep(g.node text) {
  fill: #dfe4ea !important;
}
[data-theme='dark'] .graph-container :deep(g.edge path) {
  stroke: #4a5260 !important;
}
[data-theme='dark'] .graph-container :deep(g.edge polygon) {
  fill: #4a5260 !important;
  stroke: #4a5260 !important;
}
</style>
