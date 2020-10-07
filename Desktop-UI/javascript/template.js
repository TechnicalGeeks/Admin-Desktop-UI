if(FirebaseAuth.getInstance().currentUser == null){
    // val intent = Intent(this, LoginActivity::class.java)
    // startActivity(intent)
    // finish()
    location.replace("index.html")
}else{
    Toast.makeText(this, "Already logged in", Toast.LENGTH_LONG).show()
}

let signoutbtn=document.getElementById("signout-button")

signoutbtn.addEventListener('click', button => {
    console.log("Sign Out")
    FirebaseAuth.getInstance().signOut()
    location.replace("index.html")
  });
