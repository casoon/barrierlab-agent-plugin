import type { ShowcaseExample } from '@casoon/pages-theme/showcase';

// The same files the tests compare against scripts/digest.py (tests/test_digest.py).
const files = import.meta.glob<string>('../../examples/*', {
  query: '?raw',
  import: 'default',
  eager: true,
});

const escapeHtml = (text: string) =>
  text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const examples_ = [
  {
    slug: 'page',
    title: 'A page with five failures',
    tags: ['fail', 'review', 'not checked'],
    description:
      'The report frame for `examples/page.html`: 5 failed, 8 need review, 23 not checked, 3 rules did not run. Every finding carries its line, the source line and the evidence of the engine.',
  },
  {
    slug: 'linked',
    title: 'A stylesheet the engine could not load',
    tags: ['inputs', 'not run'],
    description:
      'The page links `site.css`, which a local file run cannot resolve without `--base-url`. The frame says so before any result, and the rules that needed it are listed as not run.',
  },
];

export const examples: ShowcaseExample[] = examples_.map(({ slug, ...meta }) => ({
  slug,
  ...meta,
  file: `examples/${slug}.report.md`,
  input: { code: files[`../../examples/${slug}.html`], lang: 'html' },
  output: { html: escapeHtml(files[`../../examples/${slug}.report.md`]), kind: 'terminal' },
}));
