var http = require('http');
var formidable = require('formidable');
var fs = require('fs');

http.createServer(function (req, res) {
    if (req.url == '/fileupload') {
        var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            var oldpath = files.filetoupload.path;
            var newpath = files.filetoupload.name;
            fs.rename(oldpath, newpath, function (err) {
                if (err) throw err;
                const { exec } = require('child_process');
                exec('python execute.py', (err, stdout, stderr) => {
                    if (err) {
                        // node couldn't execute the command
                        return;
                    }
                    res.writeHead(200, {'Content-Type': 'text/plain'});
                    res.write(stdout);
                    res.end();
                });

            });
        });
    } else {
        console.log(http.version)
        console.log(formidable.version)
        console.log(fs.version)
        //console.log(exec.version)
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write("<font size='10'>")
        res.write('Welcome to the Auto-Grader System for CS1 assignment: add.py' +'</br>')
        res.write("</font>")
        res.write('</br>')
        res.write('</br>')
        res.write('Please upload you "add.py" file through the "Choose File" button below.' +'</br>')
        res.write('Once succesfully uploaded, the name of the file "add.py" will be displayed on the right of the upload button.' +'</br>')
        res.write('Please then hit "Submit" to see how your code performs.' +'</br>')
        res.write('</br>')
        res.write('</br>')
        res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
        res.write('<input type="file" name="filetoupload"><br>');
        res.write('<input type="submit">');
        res.write('</form>');
        return res.end();
    }
}).listen(8080);
