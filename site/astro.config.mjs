// @ts-check
import { readFileSync } from 'node:fs';
import casoonPages from '@casoon/pages-theme';
import { defineConfig } from 'astro/config';

// The plugin manifest is the one place the version is maintained.
const { version } = JSON.parse(readFileSync('../.claude-plugin/plugin.json', 'utf8'));

// Project page: https://casoon.github.io/barrierlab-agent-plugin/
export default defineConfig({
  site: 'https://casoon.github.io/barrierlab-agent-plugin',
  base: '/barrierlab-agent-plugin/',
  integrations: [
    casoonPages({
      name: 'barrierlab-agent-plugin',
      description:
        'A Claude Code plugin that audits a page with the barrierlab rule set and reports what failed, what needs review and what was not checked.',
      tagline: 'Accessibility audits for coding agents',
      repo: 'casoon/barrierlab-agent-plugin',
      version,
      license: 'MIT',
      catalog: false,
      docsGroups: {
        'getting-started': 'Getting started',
        reference: 'Reference',
      },
    }),
  ],
});
