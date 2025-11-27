const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const url = "https://dvet.gov.in/sites/default/files/ITI_Statistics_Maharashtra.csv";

fetch(url)
  .then(res => res.text())
  .then(csv => {
    const rows = csv.split("\n").map(r => r.split(","));
    const headers = rows[0];
    const data = rows.slice(1).map(row => {
      let obj = {};
      headers.forEach((h, i) => obj[h.trim()] = row[i]?.trim());
      return obj;
    });
    console.log("✅ ITI Data:", data);
  })
  .catch(err => console.error("❌ Error fetching CSV:", err));
