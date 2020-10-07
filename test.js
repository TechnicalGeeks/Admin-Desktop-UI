const exec= require('child_process').exec;

function execute(command,callback){
    exec(command,(error,stdout,sterr)=>{
        callback(stdout);
    });
};

execute("python FaceDetection.py 22",(output)=>{
    console.log(output);
})