// Import the http module
const http = require("http");

// Create a server
const server = http.createServer((req, res) => {

    if (req.url === "/") {
        res.setHeader("Content-Type", "text/plain");
        res.end("Welcome to the Node.js Tutorial");       // <-- end karo
    }
    else if (req.url === "/hello") {
        res.setHeader("Content-Type", "text/plain");
        res.end("Hello Saim Kazi, I am handsome!");       // <-- end karo
    }
    else if (req.url === "/saim") {
        res.setHeader("Content-Type", "text/plain");
        res.end("Hello Saim Kazi, I am handsome!");       // <-- end karo
    }
    else {
        res.statusCode = 404;
        res.setHeader("Content-Type", "text/plain");
        res.end("Page Not Found");
    }

});

// Listen on port 3000
server.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
});
