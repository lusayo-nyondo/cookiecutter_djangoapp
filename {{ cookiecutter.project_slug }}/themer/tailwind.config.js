/** @type {import('tailwindcss').Config} */
const palettes = {
  'lochmara': {
        '50': '#effaff',
        '100': '#daf3ff',
        '200': '#beebff',
        '300': '#91dfff',
        '400': '#5ecbfc',
        '500': '#38aff9',
        '600': '#2293ee',
        '700': '#1976d2',
        '800': '#1c63b1',
        '900': '#1c548c',
        '950': '#163355',
    },
}

module.exports = {
  content: [
    '*/**/*.py',
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
      colors: {
        primary: palettes['lochmara']
      },
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

