if(process.argv.length < 3){
    console.log("Usage: " + __filename + "hostname.com")
    process.exit (-1)
}

var dns = require(`dns`);

function hostnameLookup(hostname){
    dns.lookup(hostname, function(err, address, family){console.log(address);
    });

}

var hostname = process.argv [2]
console.log(`Checking IP of: ${hostname}`);
hostnameLookup(hostname);
