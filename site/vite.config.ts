import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// VITE_BASE is set in CI to the repository path for GitHub Pages, e.g. /coding-tutorial/
export default defineConfig({
  base: process.env.VITE_BASE ?? '/',
  plugins: [react()],
  worker: { format: 'es' },
})
