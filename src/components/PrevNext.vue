<script setup lang="ts">
import type { ChapterSectionRef } from '../types'

defineProps<{ prev: ChapterSectionRef | null; next: ChapterSectionRef | null }>()
</script>

<template>
  <div class="prev-next">
    <RouterLink v-if="prev" class="pn-card pn-prev" :to="prev.path">
      <span class="pn-dir">上一节</span>
      <span class="pn-title">{{ prev.title }}</span>
    </RouterLink>
    <div v-else class="pn-card pn-prev pn-disabled">
      <span class="pn-dir">上一节</span>
      <span class="pn-title">无</span>
    </div>
    <RouterLink v-if="next" class="pn-card pn-next" :to="next.path">
      <span class="pn-dir">下一节</span>
      <span class="pn-title">{{ next.title }}</span>
    </RouterLink>
    <div v-else class="pn-card pn-next pn-disabled">
      <span class="pn-dir">下一节</span>
      <span class="pn-title">无</span>
    </div>
  </div>
</template>

<style scoped>
.prev-next {
  display: flex;
  gap: 1rem;
  margin: 1.5rem 0;
}
.pn-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  padding: 0.75rem 1rem;
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  text-decoration: none;
  color: inherit;
  background: var(--surface, #fff);
}
.pn-prev {
  text-align: left;
}
.pn-next {
  text-align: right;
}
.pn-dir {
  font-size: 0.75rem;
  color: var(--muted, #888);
}
.pn-title {
  font-size: 0.95rem;
  color: var(--accent, #2563eb);
}
.pn-disabled {
  opacity: 0.5;
}
.pn-disabled .pn-title {
  color: var(--muted, #888);
}
</style>
