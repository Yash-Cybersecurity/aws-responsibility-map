import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://yash-cybersecurity.github.io',
  base: '/aws-responsibility-map',
  integrations: [tailwind()],
  output: 'static',
});