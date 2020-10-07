const exec= require('child_process').exec;

const express= require('express');
var cors = require('cors')

// const bodyParser= require('body-parser');
const app= express();
app.use(cors())
// var http= require('http');
// var server= http.createServer(app);

function execute(command,callback){
    exec(command,(error,stdout,sterr)=>{
        callback(stdout);
    });
};

// app.use(express.bodyParser.urlencoded({extended: true}));
app.post('/example',function(req,res){
    console.log("test",req.body);
    // name=req.body.name
    execute(`python FaceDetection2.py  rr`,(output)=>{
            // console.log(output);
            // outputText.innerText(output)
            res.send(output);
    });
});

const port=8081;

app.listen(port,()=>{
    console.log(`Server is running on port${port}`);
});



execute("python FaceDetection.py 22",(output)=>{
    console.log(output);
})


function pythonscript(){
    const name=form.Tname.value
    const outputText=document.getElementById('output')
    // name='rush'
    function execute(command,callback){
        exec(command,(error,stdout,sterr)=>{
            callback(error,stdout);
        });
    };
    
    execute("python FaceDetection2.py "+name,(output)=>{
        console.log(output);
        outputText.innerText(output)
    })
}