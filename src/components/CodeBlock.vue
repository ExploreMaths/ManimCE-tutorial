<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { highlightCode } from '../composables/useHighlight'

const props = withDefaults(defineProps<{ code: string; lang?: string }>(), {
  lang: 'python',
})

const highlighted = ref('')

async function update() {
  highlighted.value = await highlightCode(props.code, props.lang)
}

onMounted(update)
watch(() => [props.code, props.lang], update)
</script>

<template>
  <pre class="code-block"><code v-html="highlighted"></code></pre>
</template>

<style scoped>
.code-block {
  margin: 0;
  padding: 0.75rem 1rem;
  overflow-x: auto;
  font-size: 0.85rem;
  line-height: 1.6;
  background: var(--surface);
  border-radius: 6px;
}
</style>
