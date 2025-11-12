// Node 18+ έχει global fetch — δεν χρειάζεται axios/node-fetch.

const CITY = process.env.CITY ?? "Athens";
const STATE = process.env.STATE ?? "Attiki";
const COUNTRY = process.env.COUNTRY ?? "gr";
const API_KEY = process.env.API_KEY; // <-- πρέπει να δίνεται ως ENV

if (!API_KEY) {
  console.error("ERROR: Missing API_KEY environment variable.");
  process.exit(1);
}

const url =
  `https://api.openweathermap.org/data/2.5/weather` +
  `?q=${encodeURIComponent(CITY)},${encodeURIComponent(STATE)},${encodeURIComponent(COUNTRY)}` +
  `&appid=${encodeURIComponent(API_KEY)}`;

async function main() {
  try {
    const resp = await fetch(url, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    const text = await resp.text(); // εκτυπώνουμε όπως ήρθε
    if (!resp.ok) {
      console.error(`HTTP ${resp.status}: ${text}`);
    } else {
      console.log(text);
    }
  } catch (e) {
    console.error(e);
  }
}

console.log("Weather requester (Node.js) started ...");
setInterval(main, 60_000);
main(); // πρώτη κλήση άμεσα