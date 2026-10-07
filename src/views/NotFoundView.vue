<script setup lang="ts">
import { onMounted } from 'vue'

onMounted(() => {
  document.title = '页面不存在 · ManimCE 教程'
})
</script>

<template>
  <div class="page-narrow" style="margin: 3rem auto; text-align: center">
    <h1>404 · 页面不存在</h1>
    <p class="count-note">你访问的页面不存在或已被移动。</p>
    <RouterLink to="/" class="btn primary">返回首页</RouterLink>
  </div>
</template>
