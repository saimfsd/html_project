const http = require('http');
const server = http.createServer((req, res)=>{
res.writeHead(200, {'Content-Type': 'text/html'});

 if(req.url === "/Divya"){
    res.write('<h1>Hello, Divya</h1>');
    res.end();
    return;
 }else if(req.url == "/Alfiya"){
    res.write('<h1>Welcome Alfiya!</h1>');
    res.write('<h1>Welcome back</h1>');
    res.end();
    return;
 } 
    res.write('<h1>Hello Again , Node.js World!</h1>');
    res.end();
    
});

server.listen(4000, ()=>{

    console.log("My Server is running at http://localhost:4000/");
});