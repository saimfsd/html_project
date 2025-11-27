const API_KEY = "AIzaSyCKEVWooF6UurLr4NZ_S6CY0cZGn33y8a8";
const query = "coaching centers in Nagpur";
const url = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=${encodeURIComponent(query)}&key=${API_KEY}`;

async function fetchCoachingCenters() {
  try {
    const res = await fetch(url);
    const data = await res.json();

    console.log("Status:", data.status);
    console.log("Raw response:", data);

    if (data.results && data.results.length > 0) {
      data.results.forEach(center => {
        console.log({
          name: center.name,
          address: center.formatted_address,
          lat: center.geometry.location.lat,
          lng: center.geometry.location.lng,
          mapsLink: `https://www.google.com/maps/search/?api=1&query=${center.geometry.location.lat},${center.geometry.location.lng}`,
          rating: center.rating || "N/A"
        });
      });
    } else {
      console.log("❌ No results found.");  
    }
  } catch (err) {
    console.error("❌ Error fetching data:", err.message);
  }
}
fetchCoachingCenters();
