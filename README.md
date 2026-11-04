# Wrimble

The Wrimble website. Netlify publishes the `site` folder, and the coach runs as a Netlify Function in `netlify/functions/coach.mjs` (at `/api/coach`).

The coach needs one setting in Netlify: `ANTHROPIC_API_KEY`. Without it, the site still works and uses the built-in coach in the browser.
