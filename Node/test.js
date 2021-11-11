var hello="Hello from Node.js variable!"
var path = ("path");

console.log("Using Path mode:")
console.log(`Hello from file ${path.search(__filename)}`);

console.log(`Printing a string with a variable: ${hello}`);

console.log("directory name: " + __dirname);
console.log("directory and file: " + __filename);
console.log(`Process args: ${process.argv}`);

