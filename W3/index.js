var http = require('http');
var formidable = require('formidable');
var fs = require('fs');
var express = require('express');
var app = express();
var path = require('path');




app.use(express.urlencoded());



console.log(__dirname);
app.use(express.static(__dirname+'/assets'));

app.set('views', path.join(__dirname,'/views'));

app.set('view engine', 'ejs');

app.post("/fileupload",function (req, res) {
  
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      var oldpath = files.filetoupload.path;
      var newpath = path.join(__dirname,'./assets/pdf/song')+".pdf";
      fs.rename(oldpath, newpath, function (err) {
        if (err) throw err;
        return res.render('media');
      });
 });
});


app.get('/',function(req,res){

  return res.render('index');
});

app.listen(3000);
   