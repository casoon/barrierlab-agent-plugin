# Accessibility report: examples/page.html

Engine summary: 5 failed · 8 need review · 23 not checked · 3 rules did not run · 169 rules in the run

## 1. Failed

### `images/alt-missing` · WCAG 1.1.1 · severity high

- `images/alt-missing@14:3` (line 14, column 3): The image has no alt attribute.
  - source: `<img src="team.jpg">`

### `forms/label-missing` · WCAG 1.3.1, 3.3.2, 4.1.2 · severity critical

- `forms/label-missing@17:5` (line 17, column 5): The input has no label.
  - source: `<input type="text" name="email">`

### `links/name-missing` · WCAG 2.4.4, 4.1.2 · severity critical

- `links/name-missing@15:3` (line 15, column 3): The link has no accessible name.
  - source: `<a href="/contact"></a>`

### `buttons/name-missing` · WCAG 4.1.2 · severity critical

- `buttons/name-missing@18:5` (line 18, column 5): The button has no accessible name.
  - source: `<button></button>`

### `contrast/text-insufficient` · WCAG 1.4.3 · severity high

- `contrast/text-insufficient@13:3` (line 13, column 3): The text reaches a contrast ratio of 2.59:1; 4.5:1 is required for normal text.
  - source: `<p class="note">We answer within two days.</p>`
  - evidence (computed): contrast_ratio = 2.59
  - evidence (computed): required_ratio = 4.5

## 2. Needs review

### `headings/none` · WCAG 2.4.1 · severity low

- `headings/none@2:1` (line 2, column 1): No headings, no main landmark and no skip link; if blocks repeat across pages, nothing bypasses them.
  - source: `<html lang="en">`

### `landmarks/main-missing` · recommendation (best practice), not a violation · severity high

- `landmarks/main-missing@2:1` (line 2, column 1): The document has no main landmark.
  - source: `<html lang="en">`

### `landmarks/navigation-missing` · WCAG 1.3.1, 2.4.1 · severity low

- `landmarks/navigation-missing@2:1` (line 2, column 1): The document has no navigation landmark.
  - source: `<html lang="en">`

### `landmarks/banner-missing` · WCAG 1.3.1, 2.4.1 · severity low

- `landmarks/banner-missing@2:1` (line 2, column 1): The document has no banner landmark.
  - source: `<html lang="en">`

### `landmarks/contentinfo-missing` · WCAG 1.3.1, 2.4.1 · severity low

- `landmarks/contentinfo-missing@2:1` (line 2, column 1): The document has no contentinfo landmark.
  - source: `<html lang="en">`

### `keyboard/skip-link-missing` · WCAG 2.4.1 · severity medium

- `keyboard/skip-link-missing@2:1` (line 2, column 1): No skip link found that bypasses repeated blocks.
  - source: `<html lang="en">`

### `forms/purpose-missing` · WCAG 1.3.5 · severity medium

- `forms/purpose-missing@17:5` (line 17, column 5): The field "" seems to ask for information about the user but has no autocomplete token.
  - source: `<input type="text" name="email">`

### `landmarks/content-outside` · recommendation (best practice), not a violation · severity medium

- `landmarks/content-outside@13:3` (line 13, column 3): Content is not contained in any landmark.
  - source: `<p class="note">We answer within two days.</p>`

## 3. Not checked

### `manual/image-alternatives` · WCAG 1.1.1 · severity high

- `manual/image-alternatives@2:1` (line 2, column 1): Check by hand: every alt text says what the image means in its place, and only purely decorative images have alt="".
  - source: `<html lang="en">`

### `manual/visual-structure` · WCAG 1.3.1 · severity medium

- `manual/visual-structure@2:1` (line 2, column 1): Check by hand: what looks like a heading, list, table or menu is marked up as one — not just styled to look like it.
  - source: `<html lang="en">`

### `manual/use-of-color` · WCAG 1.4.1 · severity medium

- `manual/use-of-color@2:1` (line 2, column 1): Check by hand: colour is never the only way to tell something — links in text, required fields, errors, states.
  - source: `<html lang="en">`

### `manual/timing` · WCAG 2.2.1 · severity high

- `manual/timing@2:1` (line 2, column 1): Check by hand: any time limit can be turned off, adjusted or extended.
  - source: `<html lang="en">`

### `manual/error-handling` · WCAG 3.3.1, 3.3.3 · severity high

- `manual/error-handling@2:1` (line 2, column 1): Check by hand: submit the form with errors — each error is named in text, next to its field, with a suggestion how to fix it.
  - source: `<html lang="en">`

### `manual/no-timing` · WCAG 2.2.3 · severity low

- `manual/no-timing@2:1` (line 2, column 1): Check by hand: no task depends on timing at all, except synchronised media and real-time events.
  - source: `<html lang="en">`

### `manual/unusual-words` · WCAG 3.1.3 · severity low

- `manual/unusual-words@2:1` (line 2, column 1): Check by hand: jargon, idioms and unusual words are explained — inline, with <dfn> or in a glossary.
  - source: `<html lang="en">`

### `manual/help` · WCAG 3.3.5 · severity low

- `manual/help@2:1` (line 2, column 1): Check by hand: fields that need it have context-sensitive help — instructions, examples or a link to help.
  - source: `<html lang="en">`

### `manual/consistent-help` · WCAG 3.2.6 · severity low

- `manual/consistent-help@2:1` (line 2, column 1): Check by hand: where help is offered — contact, chat, a help page — it sits in the same place on every page of the set.
  - source: `<html lang="en">`

### `manual/keyboard-trap` · WCAG 2.1.2 · severity high

- `manual/keyboard-trap@2:1` (line 2, column 1): Check by hand: with the keyboard alone you can move into and out of every control, dialog and embedded widget again.
  - source: `<html lang="en">`

### `manual/error-prevention` · WCAG 3.3.4 · severity medium

- `manual/error-prevention@2:1` (line 2, column 1): Check by hand: submissions with legal or financial effect, or that change or delete data, can be reversed, are checked for errors, or are confirmed before they are final.
  - source: `<html lang="en">`

### `manual/consistent-navigation` · WCAG 3.2.3 · severity medium

- `manual/consistent-navigation@2:1` (line 2, column 1): Check by hand: navigation that repeats across the pages of the set keeps the same relative order.
  - source: `<html lang="en">`

### `manual/consistent-identification` · WCAG 3.2.4 · severity medium

- `manual/consistent-identification@2:1` (line 2, column 1): Check by hand: components with the same function carry the same name and the same icon on every page of the set.
  - source: `<html lang="en">`

### `manual/sensory-characteristics` · WCAG 1.3.3 · severity medium

- `manual/sensory-characteristics@2:1` (line 2, column 1): Check by hand: instructions do not rely on shape, size, position or sound alone — not just "the round button" or "the box on the right".
  - source: `<html lang="en">`

### `manual/multiple-ways` · WCAG 2.4.5 · severity medium

- `manual/multiple-ways@2:1` (line 2, column 1): Check by hand: a page of the set can be reached in more than one way — for example navigation, search, site map or related links.
  - source: `<html lang="en">`

### `manual/text-spacing` · WCAG 1.4.12 · severity medium

- `manual/text-spacing@2:1` (line 2, column 1): Check by hand: with line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 times the font size applied, no text is cut off, overlapped or lost.
  - source: `<html lang="en">`

### `order/visual-mismatch` · WCAG 1.3.2, 2.4.3 · severity low

- `order/visual-mismatch@2:1` (line 2, column 1): The host does not measure flex-direction / order; this heuristic did not run.
  - source: `<html lang="en">`

### `motion/infinite-animation` · WCAG 2.2.2 · severity low

- `motion/infinite-animation@2:1` (line 2, column 1): The host does not measure animation-iteration-count; this heuristic did not run.
  - source: `<html lang="en">`

### `reflow/min-width` · WCAG 1.4.10 · severity low

- `reflow/min-width@2:1` (line 2, column 1): The host does not measure min-width; this heuristic did not run.
  - source: `<html lang="en">`

### `keyboard/pointer-only` · WCAG 2.1.1, 4.1.2 · severity low

- `keyboard/pointer-only@2:1` (line 2, column 1): The host does not measure cursor; this heuristic did not run.
  - source: `<html lang="en">`

### `focus/obscured` · WCAG 2.4.11 · severity low

- `focus/obscured@2:1` (line 2, column 1): The host does not measure overlap with fixed or sticky elements; this heuristic did not run.
  - source: `<html lang="en">`

### `focus/indicator-unmeasured` · WCAG 2.4.7 · severity high

- `focus/indicator-unmeasured@2:1` (line 2, column 1): Focus visibility was not measured — that needs a pass that moves focus. Check by hand that every control shows keyboard focus.
  - source: `<html lang="en">`

### `keyboard/scrollable-region-not-focusable` · WCAG 2.1.1 · severity high

- `keyboard/scrollable-region-not-focusable@2:1` (line 2, column 1): The host measures no scroll extents; scrollable regions without keyboard access were not checked.
  - source: `<html lang="en">`

### Rules that did not run

- `text-spacing/clipped` · WCAG 1.4.12: capability_missing (host did not apply the text-spacing override (no text_spacing_clip))
- `focus/obscured-enhanced` · WCAG 2.4.12: capability_missing (host did not run a focus pass (no focus_cover))
- `orientation/root-rotated` · WCAG 1.3.4: capability_missing (host does not report transform or rotate of html and body)

## 4. Plan

(written by the agent, see the command)

