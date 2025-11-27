const http = require("http");
const url = require("url");
 
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const path = parsedUrl.pathname;
 
  const studentData = [
    {
      message: "Hello World",
      name: "Divya",
      age: 20,
    },
    {
      message: "Hello World",
      name: "Riya",
      age: 20,
    },
  ];
 
  const staffData = [
    {
      subject: "Programming",
      name: "Ayush Bhange",
      age: 24,
    },
    {
      subject: "DBMS",
      name: "Yash Jogekar",
      age: 24,
    },
  ];
 
  if (path === "/studentdata") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(studentData));
  } else if (path === "/staffdata") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(staffData));
  } else {
  
    res.end(JSON.stringify({ error: "Invalid Endpoint" }));
  }
});
 
server.listen(3000, () => {
  console.log("✅ Server running at http://localhost:3000/");
});
 