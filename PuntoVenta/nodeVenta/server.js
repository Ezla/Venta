var http = require('http')
var server = http.createServer().listen(3000)
var io = require('socket.io').listen(server)

var request = http.request(options, function(request){
	response.setEncoding('utf8');
	response.on('data', function(data){
		//respondiendo desde django
	});
});
request.write(values);
request.end();