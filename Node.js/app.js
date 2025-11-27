const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*'); // Allow all origins
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'); 
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization'); 

    if (req.url === "/hello") {
        res.write("<h1>Hello Welcome to my World!</h1>");
        res.end();
        return;

    } else if (req.url === "/bye") {
        res.write("<h1>Good Bye World!</h1>");
        res.end();
        return;

    } else {
        res.write("<h1>Hello, Node.js World!</h1>");
        res.end();
    }
});

server.listen(4000, () => {
    console.log("My server is running at http://localhost:4000/");
});

// const http = require('http');
 
// const server = http.createServer((req, res)=>{
// res.setHeader("Access-Control-Allow-Origin", "*"); // Allow all origins
// res.setHeader("Access-Control-Allow-Methods", "GET, POST"); // Allow specific methods
// res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization"); // Allow specific headers
 
 
//     res.writeHead(200, {'Content-Type': 'text/html'});
//      if (req.url === "/hello"){
//     res.write('<h1>Hello Node.js</h1>')
// res.end();
// return;
// }else if (req.url === "/bye"){
//     res.write(' <h1>Bye Node.js</h1>');
//     res.end();
//     return;
// }
// res.write('<h1>welcome to my server</ h1>');
// res.end();
// });
 
// server.listen(4000, ()=>{
//     console.log("Server is running at http://localhost:4000");
// });
 