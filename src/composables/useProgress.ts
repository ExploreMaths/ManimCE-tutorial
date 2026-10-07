const PROGRESS_KEY = 'mce-progress'
const SCROLL_KEY = 'mce-scroll'
const RESTORED_PREFIX = 'mce-restored'

type VisitedMap = Record<string, number>

function readJson<T>(key: string, fallback: T): T {
  try {
    const raw = localStorage.getItem(key)
    return raw ? (JSON.parse(raw) as T) : fallback
  } catch {
    return fallback
  }
}

function visitedMap(): VisitedMap {
  return readJson<VisitedMap>(PROGRESS_KEY, {})
}

function persistVisited(map: VisitedMap) {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(map))
}

export function markVisited(path: string) {
  const map = visitedMap()
  map[path] = Date.now()
  persistVisited(map)
}

export function visitedCount(): number {
  return Object.keys(visitedMap()).length
}

export function percentOf(total: number): number {
  if (total <= 0) return 0
  return Math.min(100, Math.round((visitedCount() / total) * 100))
}

function scrollMap(): Record<string, number> {
  return readJson<Record<string, number>>(SCROLL_KEY, {})
}

function persistScroll(map: Record<string, number>) {
  localStorage.setItem(SCROLL_KEY, JSON.stringify(map))
}

export function saveScroll(path: string, y: number) {
  const map = scrollMap()
  map[path] = Math.round(y)
  persistScroll(map)
}

// One-shot restore: returns the saved offset once per session per path,
// so a refresh or revisit does not double-jump.
export function takeScrollRestore(path: string): number | null {
  const flag = `${RESTORED_PREFIX}:${path}`
  if (sessionStorage.getItem(flag)) return null
  const map = scrollMap()
  const y = map[path]
  if (typeof y !== 'number') return null
  sessionStorage.setItem(flag, '1')
  return y
}

// 从头开始：清除进度、滚动记忆以及所有“已恢复”标记。
export function resetAll() {
  localStorage.removeItem(PROGRESS_KEY)
  localStorage.removeItem(SCROLL_KEY)
  for (let i = sessionStorage.length - 1; i >= 0; i--) {
    const key = sessionStorage.key(i)
    if (key && key.startsWith(RESTORED_PREFIX)) {
      sessionStorage.removeItem(key)
    }
  }
}
