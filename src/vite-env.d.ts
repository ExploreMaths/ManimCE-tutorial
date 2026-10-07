/// <reference types="vite/client" />

// highlight.js 的 exports 映射未为 ./lib/core 提供类型声明，这里补一个环境声明。
declare module 'highlight.js/lib/core' {
  import type { HLJSApi } from 'highlight.js'
  const hljs: HLJSApi
  export = hljs
}
