const exec= require('child_process').exec;

const express= require('express');
var cors = require('cors')

const bodyParser= require('body-parser');
const { log } = require('console');
const app= express();
app.use(cors())
// var http= require('http');
// var server= http.createServer(app);

function execute(command,callback){
    exec(command ,(error,stdout,sterr)=>{
        callback(stdout+error+sterr);
    });
};

app.use(bodyParser.urlencoded({extended: true}));
var output1;
app.post('/addStudent',function(req,res){
    console.log("test",req.body,req.params,req.query);
    console.log(req.body.studentName);
    var studentData={}
    for(name in req.body){
        studentData=JSON.parse(name);
    }
    name=studentData.studentName;
    clas=studentData.className;
    div=studentData.div;
    roll=studentData.rollNo;
    // res.send();

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
    execute(`python recognizer.py  ${subject} ${year_div}`,(output)=>{
        console.log(output);
        res.send(output+'<a href="index.html">GO BACK</a>');
});
})



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
