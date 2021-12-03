var os = require("os");

var total_memory = os.totalmem();
var total_mem_in_kb = total_memory/1024;
var total_mem_in_mb = total_mem_in_kb/1024;
var total_mem_in_gb = total_mem_in_mb/1024;

total_mem_in_kb = Math.floor(total_mem_in_kb);
total_mem_in_mb = Math.floor(total_mem_in_mb);
total_mem_in_gb = Math.floor(total_mem_in_gb);

total_mem_in_mb = total_mem_in_mb%1024;
total_mem_in_kb = total_mem_in_kb%1024;
total_memory = total_memory%1024;

var free_memory = os.freemem();
var free_mem_in_kb = free_memory/1024;
var free_mem_in_mb = free_mem_in_kb/1024;
var free_mem_in_gb = free_mem_in_mb/1024;

free_mem_in_kb = Math.floor(free_mem_in_kb);
free_mem_in_mb = Math.floor(free_mem_in_mb);
free_mem_in_gb = Math.floor(free_mem_in_gb);

free_mem_in_mb = free_mem_in_mb%1024;
free_mem_in_kb = free_mem_in_kb%1024;
free_memory = free_memory%1024;

var CPUs = os.cpus();
var no_of_cores = 0;

CPUs.forEach(Element =>{
    no_of_cores++;
    });

var http = require("http");
var fs = require("fs");
var ip = require("ip");



var ut_sec = os.uptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
var ut_day = ut_hour/24;

ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
ut_day = Math.floor(ut_day);

ut_day = ut_day%24;
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;

var server = http.createServer(function(req,res){
    if(req.url === "/"){
        fs.readFile("./public/index.html","UTF-8", function(err,body){
            res.writeHead(200,{"Context-Type" : "text/html"});
            res.end(body);      
        });

    }
    else if(req.url.match("/sysinfo")){
        myHostName = os.hostname();
        html=`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Node JS Response </title>
            </head>
            <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${ut_day} Days, ${ut_hour} Hrs, ${ut_min} Mins, ${ut_sec} Sec</p>
            <p>Total Memory: ${total_mem_in_mb} MB</p>
            <p>Free Memory: ${free_mem_in_mb} MB</p>
            <p>Number of CPUs: ${no_of_cores}</p>
            </body>
        </html>
        `


        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }
    else if(req.url.match("/syscode")){
        html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS System Code </title>
                </head>
                <body>
                <a href="https://github.com/uc-alexa2je/it3038c-scripts/tree/main/project2/syscode">Click here to open System code on</a>
                </body>
            </head>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);

    }

    else{
        res.writeHead(404,{"Content-Type" : "text/html"});
        res.end(`404 file not found at ${req.url}`);

    }

}).listen(3000)

console.log("Server listening on port 3000");
