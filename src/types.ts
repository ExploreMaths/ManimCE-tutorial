export interface ParamRow { name: string; type: string; default?: string; desc: string }
export interface DemoBlockData { example: string; scene: string; code: string; video: string | null; caption?: string }
export interface ChapterSectionRef { part: string; id: string; title: string; path: string }
export interface ChapterData { part: string; id: string; title: string; partTitle: string; prev: ChapterSectionRef | null; next: ChapterSectionRef | null; blocks: Block[] }
export interface PartData { id: string; title: string; sections: ChapterSectionRef[] }
export interface SiteNav { parts: PartData[]; totalSections: number }
export interface SearchItem { name: string; kind: 'class' | 'function' | 'section' | 'glossary'; path: string }
export interface ApiIndexGroup { letter: string; items: SearchItem[] }
export interface GlossaryItem { term: string; zh: string; desc: string }
export interface GraphNode { name: string; parent: string | null; link: string | null; module?: string }
export type Block =
  | { type: 'heading'; level: number; text: string; id: string }
  | { type: 'html'; html: string }
  | { type: 'params'; rows: ParamRow[] }
  | { type: 'compare'; headers: string[]; rows: string[][] }
  | { type: 'demo'; example: string; scene: string; code: string; video: string | null; caption?: string }
  | { type: 'notice'; level: 'version' | 'deprecated' | 'warning' | 'tip'; title: string; html: string }
  | { type: 'exercise'; questionHtml: string; answerHtml: string }
  | { type: 'inheritance'; chain: string[] }
