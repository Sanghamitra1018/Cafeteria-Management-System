function validate(){
    const name = document.getElementById('name').value;
    const mobile = document.getElementById('mobile').value;
    const email = document.getElementById('email').value;
 
    let error = false;
 
    
 //name
    if(name === "")
    {
     document.getElementById("name_error").innerHTML = "Name is required";                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
     error = true;
    }
    else{
     document.getElementById("name_error").innerHTML = "";
    }
 
 //mobile
 if(mobile === ""){
     document.getElementById("mobile_error").innerHTML = "Mobile number is required";
     error = true;
  }
  else if(mobile.length != 10 || isNaN(mobile)){
     document.getElementById("mobile_error").innerHTML = "please enter a 10 digit valid mobile no";
     error = true;
  }
  else{
      document.getElementById("mobile_error").innerHTML = "";
  }
  //email
  let atPos = email.indexOf('@');
  let dotPos = email.lastIndexOf('.');
  if(email === ""){
     document.getElementById("email_error").innerHTML = "email is required";
     error = true;
  }
  else if(atPos <= 0 || dotPos <= 0 || (dotPos - atPos) <= 4 || dotPos == email.lengh - 1){
     document.getElementById("email_error").innerHTML = "email is not valid!";
     error = true;
  }
  else{
     document.getElementById("email_error").innerHTML = "";
 }
 
 
    if(error)
    {
     return false;
    }
    else{
     return true;
    }
 }