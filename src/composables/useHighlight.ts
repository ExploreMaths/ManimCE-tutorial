let corePromise: Promise<typeof import('highlight.js/lib/core')> | null = null
const registeredLangs = new Set<string>()

function loadCore() {
  if (!corePromise) {
    corePromise = import('highlight.js/lib/core')
  }
  return corePromise
}

async function ensureLang(lang: string): Promise<void> {
  if (registeredLangs.has(lang)) return
  const hljs = await loadCore()
  if (lang === 'python') {
    const mod = await import('highlight.js/lib/languages/python')
    hljs.registerLanguage('python', mod.default)
  } else if (lang === 'plaintext') {
    const mod = await import('highlight.js/lib/languages/plaintext')
    hljs.registerLanguage('plaintext', mod.default)
  }
  registeredLangs.add(lang)
}

/** Highlight `code` with hljs and return the HTML string (hljs-classed spans). */
export async function highlightCode(code: string, lang = 'python'): Promise<string> {
  const hljs = await loadCore()
  const normalized = lang === 'py' ? 'python' : (lang || 'plaintext')
  try {
    await ensureLang(normalized)
  } catch {
    // language pack unavailable — fall through to plaintext
  }
  const language = registeredLangs.has(normalized) ? normalized : 'plaintext'
  try {
    return hljs.highlight(code, { language, ignoreIllegals: true }).value
  } catch {
    return hljs.highlight(code, { language: 'plaintext', ignoreIllegals: true }).value
  }
}
