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
    });
});

app.post('/signUp',function(req,res){
    console.log("## Sign Up",req.body,req.params,req.query);
    console.log(req.body.studentName);
    var signUpData={}
    for(name in req.body){
        signUpData=JSON.parse(name);
    }
    name=signUpData.facultyName;
    fid=signUpData.ID;
    email=signUpData.email;
    console.log(name+" "+fid+" "+email);
    if (signUpData.npassword==signUpData.cpassword){
        execute(`python signUp.py  ${email} ${fid} ${name} ${req.body.npassword}`,(output)=>{
                    console.log(output);
                    res.send(output);
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
    var lectureData={}
    for(name in req.body){
        lectureData=JSON.parse(name);
    }
    var subject=lectureData.subject;
    var year=lectureData.year;
    var div=lectureData.div
    console.log(subject+year+div);
    execute(`python recognizer.py  ${subject} ${year} ${div}`,(output)=>{
        console.log(output);
        res.send(output);
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
