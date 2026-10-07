<script setup lang="ts">
defineProps<{ headers: string[]; rows: string[][] }>()
</script>

<template>
  <div class="compare-scroll">
    <table class="compare-table">
      <thead>
        <tr>
          <th v-for="(h, i) in headers" :key="i">{{ h }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, r) in rows" :key="r">
          <td
            v-for="(cell, c) in row"
            :key="c"
            :class="{ first: c === 0 }"
            v-html="cell"
          ></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.compare-scroll {
  overflow-x: auto;
}
.compare-table {
  width: 100%;
  border-collapse: collapse;
}
.compare-table td.first {
  font-weight: 600;
  white-space: nowrap;
}
</style>
