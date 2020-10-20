const exec= require('child_process').exec;

const express= require('express');
var cors = require('cors')

const bodyParser= require('body-parser');
const app= express();
app.use(cors())
// var http= require('http');
// var server= http.createServer(app);

function execute(command,callback){
    exec(command,(error,stdout,sterr)=>{
        callback(stdout);
    });
};

app.use(bodyParser.urlencoded({extended: true}));
var output1;
app.post('/addStudent',function(req,res){
    console.log("test",req.body,req.params,req.query);
    name=req.body.name;
    clas=req.body.clas;
    div=req.body.div;
    roll=req.body.roll;
    execute(`python FaceDetection2.py  ${name} ${clas} ${div} ${roll}`,(output)=>{
            console.log(output);
            res.send(output);
            // res.redirect(__dirname+"try1.html")
            output1=output;
    });
});

app.post('/signUp',function(req,res){
    console.log("test",req.body,req.params,req.query);
    name=req.body.Tname;
    fid=req.body.fid;
    email=req.body.email;
    if (req.body.npassword==req.body.cpassword){
        execute(`python signUp.py  ${email} ${fid} ${name} ${req.body.npassword}`,(output)=>{
                    console.log(output);
                    res.send(output);
                    output1=output;
            });
    }
    else{
        res.send("Password Donnot Match")
    }
//     execute(`python signUp.py  ${name}`,(output)=>{
//         console.log(output);
//         res.send(output);
//         output1=output;
// });
});

app.post('/createLecture',function(req,res){
    console.log("##Create Lecture",req.body);
    var subject=req.body.status;
    var year_div=req.body.year;
    execute(`python recognizer.py  ${subject} ${year}`,(output)=>{
        console.log(output);
        res.send(output);
});
})



app.get('/example1',function(req,res){
    res.render(__dirname+"/try2.html",{output:output1});
});

const port=8081;

app.listen(port,()=>{
    console.log(`Server is running on port${port}`);
});



// execute("python FaceDetection.py 22",(output)=>{
//     console.log(output);
// })


// function pythonscript(){
//     const name=form.Tname.value
//     const outputText=document.getElementById('output')
//     // name='rush'
//     function execute(command,callback){
//         exec(command,(error,stdout,sterr)=>{
//             callback(error,stdout);
//         });
//     };
    
//     execute("python FaceDetection2.py "+name,(output)=>{
//         console.log(output);
//         outputText.innerText(output)
//     })
// }
