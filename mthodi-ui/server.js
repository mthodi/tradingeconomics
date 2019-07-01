var express = require('express');
var path = require('path');
var serverStatic = require('serve-static');
//var history = require('connect-history-api-fallback');

app = express();
app.use(serverStatic(path.join(__dirname, 'dist')));
//app.use(history());

var port = process.env.PORT || 5002;
app.listen(port);

console.log("server running on: http://127.0.0.1:" + port)
