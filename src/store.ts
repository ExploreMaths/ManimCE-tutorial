import { ref } from 'vue'
import type { SiteNav } from './types'

export const nav = ref<SiteNav | null>(null)

let navPromise: Promise<SiteNav> | null = null

export async function loadNav(): Promise<SiteNav> {
  if (nav.value) return nav.value
  if (!navPromise) {
    navPromise = fetch(`${import.meta.env.BASE_URL}data/chapters.json`)
      .then((res) => {
        if (!res.ok) throw new Error(`chapters.json: ${res.status}`)
        return res.json() as Promise<SiteNav>
      })
      .then((data) => {
        nav.value = data
        return data
      })
      .catch((err) => {
        navPromise = null
        throw err
      })
  }
  return navPromise
}

export function searchBase(): string {
  return `${import.meta.env.BASE_URL}data/`
}
