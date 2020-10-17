var config ={
  "apiKey": "AIzaSyAC4EU24xjMQKXP-41I1TnRDIT4KTN7CV8",
  "authDomain": "proxy-detection-1df22.firebaseapp.com",
  "databaseURL": "https://proxy-detection-1df22.firebaseio.com",
  "projectId": "proxy-detection-1df22",
  "storageBucket": "proxy-detection-1df22.appspot.com",
  "messagingSenderId": "17187188207",
  "appId": "1:17187188207:web:63e8c1f5b50862b1c59a1a",
  "vmeasurementId": "G-EPTQX1DS4L"
}
firebase.initializeApp(config);
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const forgotPassword= document.getElementById("forgot-password");

// loginButton.addEventListener("click", (e) => {
//     e.preventDefault();
//     const email = form.username.value;
//     const password = form.password.value;
//     const userType= form.User.value;
//     console.log(userType)
    // if(userType=="faculty")
    // {
    //   firebase.auth().signInWithEmailAndPassword(email, password).then((success)=>
    //   {
    //     alert("You have successfully logged in.");
    //     location.replace("Faculty.html")
    //   }).catch(function(error) {
    //       // Handle Errors here.
    //       var errorCode = error.code;
    //       var errorMessage = error.message;
    //       alert(errorCode+" "+errorMessage)
    //       // ...
    //     });
    // }
    // else{
    //   // if(email=="admin"&& password=="123456")
    //   // {
    //   //   alert("You have successfully logged in.");
    //   //   location.replace("Admin.html")
    //   // }
    //   firebase.auth().signInWithEmailAndPassword(email, password).then((success)=>
    //   {
    //     alert("You have successfully logged in.");
    //     location.replace("Admin.html")
    //   }).catch(function(error) {
    //       // Handle Errors here.
    //       var errorCode = error.code;
    //       var errorMessage = error.message;
    //       alert(errorCode+" "+errorMessage)
    //       // ...
    //     });
    // }

    
    // }


    function signIn(){
      const email = form.username.value;
      const password = form.password.value;
      const userType= form.User.value;
      console.log(userType)
      firebase.auth().signInWithEmailAndPassword(email, password).then((success)=>
      {
        firebase.auth().onAuthStateChanged(function(user) {
          localStorage.setItem('displayName',user.displayName)
          if(userType=="faculty"){
            alert("You have successfully logged in.");
            location.replace("Faculty.html")
          }
          else{
            if(user.uid=='Admin'){
              alert("You have successfully logged in.");
              location.replace("Admin.html");
            }
            else{
              alert("Incorrect Username or Password");
            }
          }
        })
      }).catch(function(error) {
          // Handle Errors here.
          var errorCode = error.code;
          var errorMessage = error.message;
          alert(errorCode+" "+errorMessage)
          // ...
        });
    }





    // forgotPassword.addEventListener('click',()=>{
    //   firebaseAuth.getInstance().auth.sendPasswordResetEmail(email)
    //   .addOnCompleteListener(this, OnCompleteListener { task ->
    //       if (task.isSuccessful) {
    //           Toast.makeText(this, "Reset link sent to your email", Toast.LENGTH_LONG)
    //               .show()
    //       } else {
    //           Toast.makeText(this, "Unable to send reset mail", Toast.LENGTH_LONG)
    //               .show()
    //       }
    //   })
    // })
    

      // firebase.auth().onAuthStateChanged(function(user) {
      //   if (user) {
      //     // User is signed in.
      //   } else {
      //     // No user is signed in.
      //   }
      // });

    /*if (email === "user" && password === "user") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
          firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
             // Handle Errors here.
             var errorCode = error.code;
             var errorMessage = error.message;
             // ...
           });
        loginErrorMsg.style.opacity = 1;
    }
})*/


// const login=document.querySelector('[login]')

// login.addEventListener('click',() =>{
//   const email=document.querySelector('[username]')
//   const password=document.querySelector('[password]')
//   console.log("Email :",email)
//   console.log("Password :",password)
  
//   /*firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
//     // Handle Errors here.
//     var errorCode = error.code;
//     var errorMessage = error.message;
//     // ...
//   });*/
// })




// /*firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
//     // Handle Errors here.
//     var errorCode = error.code;
//     var errorMessage = error.message;
//     // ...
// });*/