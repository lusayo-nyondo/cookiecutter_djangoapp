/** @type {import('tailwindcss').Config} */
const colorPalettes = require('./__themer.js');

module.exports = {
  content: [
    '../*/**/*.py',
    '../templates/**/*.{html,svg}',
    '../*/templates/**/*.{html,svg}',
    '../*/components/**/*.{html,py,js,css}',
    '../static/js/*.{js,mjs,cjs}',
    '../static/css/input.css',
    '!venv',
    '!node_modules',
  ],
  theme: {
    extend: {
      colors: colorPalettes,
      gridTemplateColumns: {
        '18': 'repeat(18, minmax(0, 1fr))',
        '17': 'repeat(17, minmax(0, 1fr))',
      },
      gridColumn: {
        'span-17': 'span 17 / span 17',
      }
    },
  },
  plugins: [],
}

