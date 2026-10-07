<script setup lang="ts">
defineProps<{ items: { label: string; to?: string }[] }>()
</script>

<template>
  <nav aria-label="面包屑">
    <ol class="breadcrumb">
      <li v-for="(item, i) in items" :key="i">
        <RouterLink v-if="item.to && i < items.length - 1" :to="item.to">{{ item.label }}</RouterLink>
        <span v-else :aria-current="i === items.length - 1 ? 'page' : undefined">{{ item.label }}</span>
        <span v-if="i < items.length - 1" class="sep">/</span>
      </li>
    </ol>
  </nav>
</template>

<style scoped>
.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  list-style: none;
  margin: 0;
  padding: 0;
  font-size: 0.85rem;
  color: var(--muted, #888);
}
.breadcrumb a {
  color: var(--muted, #888);
  text-decoration: none;
}
.breadcrumb a:hover {
  color: var(--accent, #2563eb);
}
.breadcrumb span[aria-current] {
  color: var(--text, #222);
}
.sep {
  margin-left: 0.4rem;
}
</style>
