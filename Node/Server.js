var http = require("http");

var server = http.createServer(function(req,res){
    res.writeHead(200, {"Content-Type" : "text/html"});
    res.end(`
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS response</title>
                </head>
                <body>
                    <h1>Node JS test!</h1>
                    <p>${req.url}</p>
                    <p>${req.method}</p>
                </body>
        </html>  
    
    `)});

    server.listen(3000)

    console.log("Server listening on port 3000");
