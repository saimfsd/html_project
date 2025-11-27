// Import http module
const http = require("http");

// Create server
const server = http.createServer((req, res) => {

    // CORS fix: allow all
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");

    // ROUTES
    if (req.url === "/hello") {
        res.statusCode = 200;
        res.setHeader("Content-Type", "text/plain");
        res.end("Hello Saim! Backend is working properly.");
    }
    else {
        res.statusCode = 404;
        res.setHeader("Content-Type", "text/plain");
        res.end("Page Not Found");
    }
});

// Listen on port 4000
server.listen(4000, () => {
    console.log("Server running at http://localhost:4000");
});
