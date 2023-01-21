/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}",],
  theme: {
    extend: {
      fontFamily: {
        'Outfit': ['Outfit', 'sans-serif'],
        'Source-Sans':['Source Sans Pro', 'sans-serif']
      }
    },
  },
  plugins: [],
}
