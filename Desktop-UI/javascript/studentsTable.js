


// var config ={
//     "apiKey": "AIzaSyAC4EU24xjMQKXP-41I1TnRDIT4KTN7CV8",
//     "authDomain": "proxy-detection-1df22.firebaseapp.com",
//     "databaseURL": "https://proxy-detection-1df22.firebaseio.com",
//     "projectId": "proxy-detection-1df22",
//     "storageBucket": "proxy-detection-1df22.appspot.com",
//     "messagingSenderId": "17187188207",
//     "appId": "1:17187188207:web:63e8c1f5b50862b1c59a1a",
//     "vmeasurementId": "G-EPTQX1DS4L"
// }
// firebase.initializeApp(config);

const preObject=document.getElementById('object');
var table=document.getElementById('student-table')
var headings=[];
for (let index = 0; index < 5; index++) {
    headings.push(document.getElementById('subject'+String(index+1)));
    
}
var content='';



function retrieve(){
    console.log('test')
    var IClass=document.getElementById('year').value;
    var IDiv=document.getElementById('div').value;
    // for (let index = 0; index < 5; index++) {
    //     headings.push(document.getElementById('subject'+String(index+1)));
        
    // }
    
    console.log('Class'+IClass);
    console.log('Division'+IDiv);

    const dbRefObject=firebase.database().ref().child(IClass);
    
    dbRefObject.on('value', snap=> {
        console.log(snap.val())
        var data=snap.val();
        // console.log(data[IDiv]['18'])
        var students=Object.keys(data[IDiv]);
        console.log(students);
    
        var subjects=Object.keys(data[IDiv][students[0]])
        console.log(subjects);
        
        table.innerHTML=''
        content=''
        console.log(table.innerHTML)
        content+='<thead>'
        content+='<th>Roll No.</th>'
        for (let i = 0; i < subjects.length; i++) {
            content+='<th>'+subjects[i]+'</th>'
            
        }
        content+='</thead>'
        
        for (let index = 0; index < students.length; index++) {
            content +='<tr>';
            content += '<td>' + students[index]+ '</td>';
            for (let i = 0; i < subjects.length; i++) {
                content += '<td>' + data[IDiv][students[index]][subjects[i]]+ '</td>';
            }
            content += '</tr>';
            
        }
        table.innerHTML+=content;
    
    
    });
    
}



// // Get a reference to the database service
// var database = firebase.database();

// var starCountRef = firebase.database().ref('posts/' + postId + '/starCount');
// starCountRef.on('value', function(snapshot) {
//   updateStarCount(postElement, snapshot.val());
  
//   var userId = firebase.auth().currentUser.uid;
//   return firebase.database().ref('/users/' + userId).once('value').then(function(snapshot) {
//   var username = (snapshot.val() && snapshot.val().username) || 'Anonymous';
//   console.log(username)
//   // ...
// });
// });

// var userId = firebase.auth().currentUser.uid;
// return firebase.database().ref('/users/' + userId).once('value').then(function(snapshot) {
//   var username = (snapshot.val() && snapshot.val().username) || 'Anonymous';
//   console.log(username)
//   // ...
// });