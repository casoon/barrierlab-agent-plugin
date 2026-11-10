# Accessibility report: examples/linked.html

Engine summary: 1 failed · 4 need review · 14 not checked · 2 rules did not run · 169 rules in the run

## Inputs the engine could not use

- stylesheet_unavailable: `site.css` (no base URL for a local file; pass --base-url)

## 1. Failed

### `images/alt-missing` · WCAG 1.1.1 · severity high

- `images/alt-missing@3:35` (line 3, column 35): The image has no alt attribute.
  - source: `<body><main><h1>T</h1><p>Hello</p><img src="a.png"></main></body></html>`

## 2. Needs review

### `zoom/viewport-missing` · recommendation (best practice), not a violation · severity high

- `zoom/viewport-missing@2:1` (line 2, column 1): The document has no viewport declaration.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `landmarks/navigation-missing` · WCAG 1.3.1, 2.4.1 · severity low

- `landmarks/navigation-missing@2:1` (line 2, column 1): The document has no navigation landmark.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `landmarks/banner-missing` · WCAG 1.3.1, 2.4.1 · severity low

- `landmarks/banner-missing@2:1` (line 2, column 1): The document has no banner landmark.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `landmarks/contentinfo-missing` · WCAG 1.3.1, 2.4.1 · severity low

- `landmarks/contentinfo-missing@2:1` (line 2, column 1): The document has no contentinfo landmark.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

## 3. Not checked

### `manual/image-alternatives` · WCAG 1.1.1 · severity high

- `manual/image-alternatives@2:1` (line 2, column 1): Check by hand: every alt text says what the image means in its place, and only purely decorative images have alt="".
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `manual/visual-structure` · WCAG 1.3.1 · severity medium

- `manual/visual-structure@2:1` (line 2, column 1): Check by hand: what looks like a heading, list, table or menu is marked up as one — not just styled to look like it.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `manual/unusual-words` · WCAG 3.1.3 · severity low

- `manual/unusual-words@2:1` (line 2, column 1): Check by hand: jargon, idioms and unusual words are explained — inline, with <dfn> or in a glossary.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `manual/consistent-help` · WCAG 3.2.6 · severity low

- `manual/consistent-help@2:1` (line 2, column 1): Check by hand: where help is offered — contact, chat, a help page — it sits in the same place on every page of the set.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `manual/sensory-characteristics` · WCAG 1.3.3 · severity medium

- `manual/sensory-characteristics@2:1` (line 2, column 1): Check by hand: instructions do not rely on shape, size, position or sound alone — not just "the round button" or "the box on the right".
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `manual/text-spacing` · WCAG 1.4.12 · severity medium

- `manual/text-spacing@2:1` (line 2, column 1): Check by hand: with line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 times the font size applied, no text is cut off, overlapped or lost.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `contrast/text-undetermined` · WCAG 1.4.3 · severity medium

- `contrast/text-undetermined@3:13` (line 3, column 13): The contrast cannot be determined automatically — the host could not resolve the foreground or background colour. Check it by hand.
  - source: `<body><main><h1>T</h1><p>Hello</p><img src="a.png"></main></body></html>`
- `contrast/text-undetermined@3:23` (line 3, column 23): The contrast cannot be determined automatically — the host could not resolve the foreground or background colour. Check it by hand.
  - source: `<body><main><h1>T</h1><p>Hello</p><img src="a.png"></main></body></html>`

### `order/visual-mismatch` · WCAG 1.3.2, 2.4.3 · severity low

- `order/visual-mismatch@2:1` (line 2, column 1): The host does not measure flex-direction / order; this heuristic did not run.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `motion/infinite-animation` · WCAG 2.2.2 · severity low

- `motion/infinite-animation@2:1` (line 2, column 1): The host does not measure animation-iteration-count; this heuristic did not run.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `reflow/min-width` · WCAG 1.4.10 · severity low

- `reflow/min-width@2:1` (line 2, column 1): The host does not measure min-width; this heuristic did not run.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `keyboard/pointer-only` · WCAG 2.1.1, 4.1.2 · severity low

- `keyboard/pointer-only@2:1` (line 2, column 1): The host does not measure cursor; this heuristic did not run.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `focus/obscured` · WCAG 2.4.11 · severity low

- `focus/obscured@2:1` (line 2, column 1): The host does not measure overlap with fixed or sticky elements; this heuristic did not run.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### `keyboard/scrollable-region-not-focusable` · WCAG 2.1.1 · severity high

- `keyboard/scrollable-region-not-focusable@2:1` (line 2, column 1): The host measures no scroll extents; scrollable regions without keyboard access were not checked.
  - source: `<html lang="en"><head><title>T</title><link rel="stylesheet" href="site.css"></head>`

### Rules that did not run

- `text-spacing/clipped` · WCAG 1.4.12: capability_missing (host did not apply the text-spacing override (no text_spacing_clip))
- `orientation/root-rotated` · WCAG 1.3.4: capability_missing (host does not report transform or rotate of html and body)

## 4. Plan

(written by the agent, see the command)

