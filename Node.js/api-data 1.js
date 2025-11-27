// Training Centers API using Google Places API
// Install required packages: npm install express axios dotenv cors

const express = require('express');
const axios = require('axios');
require('dotenv').config();
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Google Places API Key - Get from: https://console.cloud.google.com/
const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY || 'YOUR_API_KEY_HERE';

// Search Training Centers
app.get('/api/training-centers', async (req, res) => {
  try {
    const { location = 'Nagpur', type = 'training center', radius = 5000 } = req.query;
    
    // Step 1: Get coordinates of location
    const geocodeUrl = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(location)}&key=${GOOGLE_API_KEY}`;
    const geoResponse = await axios.get(geocodeUrl);
    
    if (geoResponse.data.results.length === 0) {
      return res.status(404).json({ error: 'Location not found' });
    }
    
    const { lat, lng } = geoResponse.data.results[0].geometry.location;
    
    // Step 2: Search nearby training centers
    const placesUrl = `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${lng}&radius=${radius}&keyword=${encodeURIComponent(type)}&key=${GOOGLE_API_KEY}`;
    const placesResponse = await axios.get(placesUrl);
    
    // Step 3: Get detailed information for each place
    const detailedResults = await Promise.all(
      placesResponse.data.results.slice(0, 10).map(async (place) => {
        const detailsUrl = `https://maps.googleapis.com/maps/api/place/details/json?place_id=${place.place_id}&fields=name,formatted_address,formatted_phone_number,website,rating,opening_hours,types&key=${GOOGLE_API_KEY}`;
        const detailsResponse = await axios.get(detailsUrl);
        const details = detailsResponse.data.result;
        
        return {
          id: place.place_id,
          name: details.name || 'N/A',
          type: place.types?.join(', ') || 'Training Center',
          address: details.formatted_address || 'N/A',
          phone: details.formatted_phone_number || 'N/A',
          website: details.website || 'N/A',
          rating: details.rating || 'N/A',
          location: {
            lat: place.geometry.location.lat,
            lng: place.geometry.location.lng
          },
          isOpen: details.opening_hours?.open_now || 'Unknown'
        };
      })
    );
    
    res.json({
      success: true,
      count: detailedResults.length,
      location: location,
      data: detailedResults
    });
    
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ 
      success: false, 
      error: 'Failed to fetch training centers',
      message: error.message 
    });
  }
});

// Search by keyword
app.get('/api/search', async (req, res) => {
  try {
    const { query, location = 'Nagpur' } = req.query;
    
    if (!query) {
      return res.status(400).json({ error: 'Query parameter is required' });
    }
    
    const searchUrl = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=${encodeURIComponent(query + ' in ' + location)}&key=${GOOGLE_API_KEY}`;
    const response = await axios.get(searchUrl);
    
    const results = response.data.results.map(place => ({
      id: place.place_id,
      name: place.name,
      address: place.formatted_address,
      rating: place.rating || 'N/A',
      location: place.geometry.location
    }));
    
    res.json({
      success: true,
      count: results.length,
      data: results
    });
    
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ 
      success: false, 
      error: 'Search failed',
      message: error.message 
    });
  }
});

// Alternative: Use Yelp API
app.get('/api/yelp/training-centers', async (req, res) => {
  try {
    const YELP_API_KEY = process.env.YELP_API_KEY || 'YOUR_YELP_API_KEY';
    const { location = 'Nagpur, India', term = 'training center' } = req.query;
    
    const yelpUrl = 'https://api.yelp.com/v3/businesses/search';
    const response = await axios.get(yelpUrl, {
      headers: {
        'Authorization': `Bearer ${YELP_API_KEY}`
      },
      params: {
        term: term,
        location: location,
        limit: 20
      }
    });
    
    const results = response.data.businesses.map(business => ({
      id: business.id,
      name: business.name,
      phone: business.phone || 'N/A',
      address: business.location.display_address.join(', '),
      city: business.location.city,
      rating: business.rating,
      url: business.url,
      categories: business.categories.map(cat => cat.title).join(', ')
    }));
    
    res.json({
      success: true,
      count: results.length,
      data: results
    });
    
  } catch (error) {
    console.error('Yelp Error:', error.message);
    res.status(500).json({ 
      success: false, 
      error: 'Yelp API failed',
      message: error.message 
    });
  }
});

// Mock API (No external API needed)
app.get('/api/mock/training-centers', (req, res) => {
  const mockData = [
    {
      id: 1,
      name: "Tech Skills Academy Nagpur",
      type: "IT Training",
      email: "info@techskills.com",
      phone: "+91 98765 43210",
      address: "123 MG Road, Sitabuldi, Nagpur",
      location: "Nagpur, Maharashtra 440001",
      website: "www.techskills.com",
      courses: ["Web Development", "Data Science", "Python", "Java"]
    },
    {
      id: 2,
      name: "Professional Skill Development Center",
      type: "Vocational Training",
      email: "contact@psdc.in",
      phone: "+91 97654 32109",
      address: "456 Civil Lines, Nagpur",
      location: "Nagpur, Maharashtra 440001",
      website: "www.psdc.in",
      courses: ["Accounting", "Business Management", "English Speaking"]
    },
    {
      id: 3,
      name: "Coding Bootcamp India",
      type: "IT Training",
      email: "hello@codingbootcamp.in",
      phone: "+91 96543 21098",
      address: "789 Dharampeth, Nagpur",
      location: "Nagpur, Maharashtra 440010",
      website: "www.codingbootcamp.in",
      courses: ["Full Stack Development", "Mobile App Dev", "Cloud Computing"]
    }
  ];
  
  res.json({
    success: true,
    count: mockData.length,
    data: mockData
  });
});

// Health check
app.get('/', (req, res) => {
  res.json({ 
    message: 'Training Centers API is running',
    endpoints: {
      'GET /api/training-centers': 'Get training centers (Google Places)',
      'GET /api/search?query=coding': 'Search by keyword',
      'GET /api/yelp/training-centers': 'Get training centers (Yelp)',
      'GET /api/mock/training-centers': 'Get mock data (no API key needed)'
    }
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
  console.log(`
Setup Instructions:
1. npm install express axios dotenv cors
2. Create .env file with:
   GOOGLE_API_KEY=your_google_api_key
   YELP_API_KEY=your_yelp_api_key
3. Get Google API key: https://console.cloud.google.com/
4. Get Yelp API key: https://www.yelp.com/developers
5. Run: node server.js
  `);
});