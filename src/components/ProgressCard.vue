<script setup lang="ts">
defineProps<{ percent: number; visited: number; total: number }>()

const emit = defineEmits<{ (e: 'reset'): void }>()

function onReset() {
  if (window.confirm('清除全部学习进度并从头开始？')) {
    emit('reset')
  }
}
</script>

<template>
  <div class="card progress-card">
    <div class="progress-text">已完成 {{ visited }} / {{ total }} 节 ({{ percent }}%)</div>
    <div class="progress-track">
      <div class="progress-fill" :style="{ width: percent + '%' }"></div>
    </div>
    <button class="progress-reset" type="button" @click="onReset">从头开始</button>
  </div>
</template>

<style scoped>
.progress-card {
  padding: 0.9rem 1rem;
}
.progress-text {
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}
.progress-track {
  height: 6px;
  border-radius: 3px;
  background: var(--border, #ddd);
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: var(--accent, #2563eb);
  transition: width 0.3s;
}
.progress-reset {
  margin-top: 0.6rem;
  font-size: 0.8rem;
  padding: 0.25rem 0.7rem;
  border: 1px solid var(--border, #ddd);
  border-radius: 4px;
  background: transparent;
  color: var(--muted, #888);
  cursor: pointer;
}
.progress-reset:hover {
  color: var(--accent, #2563eb);
  border-color: var(--accent, #2563eb);
}
</style>
