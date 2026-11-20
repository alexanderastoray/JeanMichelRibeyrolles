// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://jeanmichelribeyrolles.fr',
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
});
