<script setup lang="ts">
defineProps<{ questionHtml: string; answerHtml: string }>()
</script>

<template>
  <div class="exercise-block">
    <div class="exercise-tag">练习</div>
    <div class="exercise-question" v-html="questionHtml"></div>
    <details class="exercise-answer">
      <summary>参考答案</summary>
      <div v-html="answerHtml"></div>
    </details>
  </div>
</template>

<style scoped>
.exercise-block {
  border: 1px solid var(--border, #ddd);
  border-radius: 6px;
  padding: 0.75rem 1rem;
  margin: 1rem 0;
  background: var(--surface, #fafafa);
}
.exercise-tag {
  display: inline-block;
  font-size: 0.72rem;
  padding: 0.1rem 0.5rem;
  border-radius: 4px;
  background: var(--accent, #2563eb);
  color: #fff;
  margin-bottom: 0.5rem;
}
.exercise-question {
  line-height: 1.7;
}
.exercise-answer {
  margin-top: 0.5rem;
  font-size: 0.9rem;
}
.exercise-answer summary {
  cursor: pointer;
  color: var(--accent, #2563eb);
}
</style>
