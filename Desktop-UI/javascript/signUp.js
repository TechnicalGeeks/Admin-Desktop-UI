function signUp(){
    var displayName=document.getElementById('Tname').value;
    var facultyID=document.getElementById('fid').value;
    var email=document.getElementById('email').value;
    var newPassword=document.getElementById('npassword').value;
    var confirmPassword=document.getElementById('npassword').value;
    console.log(newPassword+" "+confirmPassword);
    console.log(email);
    if(newPassword==confirmPassword){
        firebase.auth().createUserWithEmailAndPassword(email, newPassword).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            // ...
          });
        //   user.updateProfile({
        //     displayName: displayName,
        //     uid: facultyID
        //   }).then(function() {
        //     // Update successful.
        //   }).catch(function(error) {
        //     // An error happened.
        //   });
    }
    else{
        alert('Password Donnot Match !!!')
    }
    
}
