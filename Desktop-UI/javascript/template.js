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

  var Username=document.getElementById('user');

  firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
              // User is signed in.
              // var displayName = user.displayName;
              // var email = user.email;
            //   var emailVerified = user.emailVerified;
            //   var photoURL = user.photoURL;
            //   var isAnonymous = user.isAnonymous;
              // var uid = user.uid;
            //   var providerData = user.providerData;
              // ...
              console.log(localStorage.getItem('displayName'));
              Username.innerHTML=localStorage.getItem('displayName');
              var anchor=document.getElementById('goBack')
              if(localStorage.getItem('displayName')=='Admin'){
                  anchor.href='Admin.html'
              }
              else{
                  anchor.href='Faculty.html'
              }
            } else {
              // User is signed out.
              // ...
              console.log("Sign Out")
              location.replace("index.html")
            }
          });
//   if(FirebaseAuth.getInstance().currentUser == null){
//     // val intent = Intent(this, LoginActivity::class.java)
//     // startActivity(intent)
//     // finish()
//     location.replace("index.html")
// }else{
//     Toast.makeText(this, "Already logged in", Toast.LENGTH_LONG).show()
// }

// let signoutbtn=document.getElementById("signout-button")

function signOut(){
    firebase.auth().signOut().then(function() {
        // Sign-out successful.
        console.log("Sign Out");
        location.replace("index.html");
      }).catch(function(error) {
        // An error happened.
        alert(error.code+error.message);
      });
    // console.log("Sign Out")
    // FirebaseAuth.getInstance().signOut()
    // location.replace("index.html")
};

