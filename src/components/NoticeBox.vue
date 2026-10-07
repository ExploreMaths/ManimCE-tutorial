<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  level: 'version' | 'deprecated' | 'warning' | 'tip'
  title?: string
  html: string
}>()

const META: Record<string, { label: string; color: string }> = {
  version: { label: '版本变更', color: '#2563eb' },
  deprecated: { label: '弃用', color: '#d97706' },
  warning: { label: '注意', color: '#dc2626' },
  tip: { label: '提示', color: '#16a34a' },
}

const meta = computed(() => META[props.level])
</script>

<template>
  <div class="notice-box" :style="{ borderColor: meta.color }">
    <div class="notice-head">
      <span class="notice-label" :style="{ background: meta.color }">{{ meta.label }}</span>
      <strong v-if="title" class="notice-title">{{ title }}</strong>
    </div>
    <div class="notice-body" v-html="html"></div>
  </div>
</template>

<style scoped>
.notice-box {
  border: 1px solid;
  border-left-width: 4px;
  border-radius: 6px;
  padding: 0.75rem 1rem;
  margin: 1rem 0;
  background: var(--surface, #fafafa);
}
.notice-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.25rem;
}
.notice-label {
  color: #fff;
  font-size: 0.72rem;
  padding: 0.1rem 0.45rem;
  border-radius: 4px;
}
.notice-title {
  font-size: 0.95rem;
}
.notice-body {
  font-size: 0.9rem;
  line-height: 1.7;
}
</style>
