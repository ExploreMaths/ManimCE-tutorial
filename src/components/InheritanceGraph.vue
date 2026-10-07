<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import type { GraphNode } from '../types'

const props = defineProps<{ nodes: GraphNode[] }>()
const router = useRouter()

const NODE_W = 150
const NODE_H = 34
const COL_W = 190
const ROW_H = 46
const PAD = 8

const byName = computed(() => {
  const map = new Map<string, GraphNode>()
  for (const n of props.nodes) map.set(n.name, n)
  return map
})

const childrenOf = computed(() => {
  const map = new Map<string, GraphNode[]>()
  for (const n of props.nodes) {
    if (n.parent) {
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

const depthOf = computed(() => {
  const map = new Map<string, number>()
  function depth(name: string, visiting: Set<string>): number {
    const cached = map.get(name)
    if (cached !== undefined) return cached
    if (visiting.has(name)) return 0
    visiting.add(name)
    const node = byName.value.get(name)
    let d = 0
    if (node?.parent && byName.value.has(node.parent)) {
      d = depth(node.parent, visiting) + 1
    }
    visiting.delete(name)
    map.set(name, d)
    return d
  }
  for (const n of props.nodes) depth(n.name, new Set())
  return map
})

const collapsed = ref<Set<string>>(new Set())

const visible = computed(() => {
  const set = new Set<string>()
  const queue: string[] = roots.value.map((r) => r.name)
  while (queue.length) {
    const name = queue.shift()!
    if (set.has(name)) continue
    set.add(name)
    if (collapsed.value.has(name)) continue
    for (const child of childrenOf.value.get(name) ?? []) {
      queue.push(child.name)
    }
  }
  return set
})

const layout = computed(() => {
  const pos = new Map<string, { x: number; y: number }>()
  const columns = new Map<number, GraphNode[]>()
  for (const n of props.nodes) {
    if (!visible.value.has(n.name)) continue
    const d = depthOf.value.get(n.name) ?? 0
    const list = columns.get(d) ?? []
    list.push(n)
    columns.set(d, list)
  }
  let maxDepth = 0
  let maxRows = 1
  for (const [d, list] of columns) {
    maxDepth = Math.max(maxDepth, d)
    maxRows = Math.max(maxRows, list.length)
    list.forEach((n, row) => {
      pos.set(n.name, { x: PAD + d * COL_W, y: PAD + row * ROW_H })
    })
  }
  return {
    pos,
    width: (maxDepth + 1) * COL_W + PAD,
    height: maxRows * ROW_H + PAD * 2,
    maxDepth,
  }
})

const edges = computed(() => {
  const list: { d: string; from: string; to: string }[] = []
  for (const n of props.nodes) {
    if (!n.parent) continue
    if (!visible.value.has(n.name) || !visible.value.has(n.parent)) continue
    const a = layout.value.pos.get(n.parent)
    const b = layout.value.pos.get(n.name)
    if (!a || !b) continue
    const x1 = a.x + NODE_W
    const y1 = a.y + NODE_H / 2
    const x2 = b.x
    const y2 = b.y + NODE_H / 2
    const dx = Math.max(30, (x2 - x1) / 2)
    list.push({
      from: n.parent,
      to: n.name,
      d: `M ${x1} ${y1} C ${x1 + dx} ${y1}, ${x2 - dx} ${y2}, ${x2} ${y2}`,
    })
  }
  return list
})

const filter = ref('')
const dimmed = computed(() => {
  const q = filter.value.trim().toLowerCase()
  if (!q) return new Set<string>()
  return new Set(
    props.nodes.filter((n) => !n.name.toLowerCase().includes(q)).map((n) => n.name),
  )
})

function hasChildren(name: string) {
  return (childrenOf.value.get(name) ?? []).length > 0
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

function displayName(name: string) {
  return name.length > 22 ? name.slice(0, 21) + '…' : name
}

function onNodeClick(node: GraphNode) {
  if (node.link) router.push(node.link)
  else toggle(node.name)
}

function nodeFill(name: string) {
  return dimmed.value.has(name) ? 0.25 : 1
}

const displayNodes = computed(() => {
  const list: { node: GraphNode; x: number; y: number; isRoot: boolean }[] = []
  for (const n of props.nodes) {
    if (!visible.value.has(n.name)) continue
    const p = layout.value.pos.get(n.name)
    if (!p) continue
    list.push({ node: n, x: p.x, y: p.y, isRoot: (depthOf.value.get(n.name) ?? 0) === 0 })
  }
  return list
})
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
    <div class="graph-scroll">
      <svg
        :width="layout.width"
        :height="layout.height"
        :viewBox="`0 0 ${layout.width} ${layout.height}`"
        role="img"
        aria-label="继承关系图"
      >
        <path
          v-for="e in edges"
          :key="e.from + '->' + e.to"
          :d="e.d"
          fill="none"
          :stroke="'var(--border, #ccc)'"
          stroke-width="1.5"
          :opacity="dimmed.has(e.from) || dimmed.has(e.to) ? 0.15 : 1"
        />
        <g v-for="item in displayNodes" :key="item.node.name">
          <rect
            :x="item.x"
            :y="item.y"
            :width="NODE_W"
            :height="NODE_H"
            rx="6"
            :fill="'var(--surface, #fff)'"
            :stroke="item.isRoot ? 'var(--accent, #2563eb)' : 'var(--border, #ccc)'"
            :stroke-width="item.isRoot ? 2 : 1"
            :opacity="nodeFill(item.node.name)"
            style="cursor: pointer"
            @click="toggle(item.node.name)"
          />
          <text
            :x="item.x + 8"
            :y="item.y + NODE_H / 2 + 4"
            font-size="11"
            :fill="'var(--text, #222)'"
            :opacity="nodeFill(item.node.name)"
            style="cursor: pointer"
            @click.stop="onNodeClick(item.node)"
          >
            {{ displayName(item.node.name) }}
          </text>
          <g
            v-if="hasChildren(item.node.name)"
            :transform="`translate(${item.x + NODE_W - 4}, ${item.y})`"
            style="cursor: pointer"
            @click.stop="toggle(item.node.name)"
          >
            <circle r="7" :fill="'var(--accent, #2563eb)'" />
            <text y="3.5" text-anchor="middle" font-size="11" fill="#fff">
              {{ collapsed.has(item.node.name) ? '+' : '−' }}
            </text>
          </g>
        </g>
      </svg>
    </div>
  </div>
</template>

<style scoped>
.graph-wrap {
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  background: var(--surface, #fff);
  padding: 0.5rem;
}
.graph-toolbar {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  margin-bottom: 0.5rem;
}
.graph-filter {
  flex: 1;
  max-width: 260px;
  padding: 0.25rem 0.6rem;
  font-size: 0.82rem;
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  background: var(--bg, #fff);
  color: var(--text, #222);
}
.graph-toolbar button {
  font-size: 0.8rem;
  padding: 0.25rem 0.7rem;
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  background: transparent;
  color: var(--text, #222);
  cursor: pointer;
}
.graph-toolbar button:hover {
  color: var(--accent, #2563eb);
  border-color: var(--accent, #2563eb);
}
.graph-scroll {
  overflow-x: auto;
}
</style>
