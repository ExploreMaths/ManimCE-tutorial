#!/usr/bin/env node
// Copy build_content.py output (src/data) into dist/ after vite build.
// vite only bundles imported modules and public/, so the JSON data tree
// would otherwise never reach dist/ (fetch then hits the SPA fallback
// and fails to parse HTML as JSON).

import { cpSync, existsSync } from 'node:fs'

const src = 'src/data'
const dest = 'dist/data'

if (!existsSync(src)) {
  console.error(`copy-data: ${src} not found — run scripts/build_content.py first`)
  process.exit(1)
}

cpSync(src, dest, { recursive: true })
console.log(`copy-data: ${src} -> ${dest}`)
