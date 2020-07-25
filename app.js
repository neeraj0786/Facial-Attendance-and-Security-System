// import express JS module into app
// and creates its variable.
var express = require('express');
var app = express();

// Creates a server which runs on port 3000 and
// can be accessed through localhost:3000
app.listen(3000, function() {
	console.log('server running on port 3000');
} )

// Function callName() is executed whenever
// url is of the form localhost:3000/name
app.get('/', callName);

function callName(req, res) {
   // res.redirect('https://us04web.zoom.us/j/3100988987?pwd=oeoDAU6FX1A');
	// Use child_process.spawn method from
	// child_process module and assign it
	// to variable spawn

	var spawn = require("child_process").spawn;
    let matched=false;
	// Parameters passed in spawn -
	// 1. type_of_script
	// 2. list containing Path of the script
	// and arguments for the script
    var process = spawn('python',["./attendanceProject.py"]);

    process.on('exit', (code,matched)=>{
    if(code === 1)
    matched = true;
    else matched=false;
    console.log(matched,code);
    if(matched) res.redirect('https://us04web.zoom.us/j/3100988987?pwd=oeoDAU6FX1A');
    else res.redirect('https://www.google.com');
    })




	// E.g : http://localhost:3000/name?firstname=Mike&lastname=Will
	// so, first name = Mike and last name = Will

	// Takes stdout data from script which executed
	// with arguments and send this data to res object
	/*process.stdout.on('data', function(data) {
		res.send(data.toString());
	} );*/

}


