<script setup lang="ts">
import type { ParamRow } from '../types'

defineProps<{ rows: ParamRow[] }>()
</script>

<template>
  <div class="card">
    <table class="param-table">
      <thead>
        <tr>
          <th>参数</th>
          <th>类型</th>
          <th>默认值</th>
          <th>说明</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.name">
          <td class="mono" v-html="row.name"></td>
          <td class="mono" v-html="row.type"></td>
          <td class="mono" v-html="row.default ?? '—'"></td>
          <td v-html="row.desc"></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.param-table {
  width: 100%;
  border-collapse: collapse;
}
.mono {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.85em;
  white-space: nowrap;
}
</style>
