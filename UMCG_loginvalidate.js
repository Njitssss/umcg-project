function signIn(){
    var signupEmail = document.getElementById("signupEmail").value;
    var signupPassword = document.getElementById("signupPassword").value;

    if(signupEmail == "admin@hotmail.nl" && signupPassword == "admin123")
    {
        location.replace("UMCG_homepage.html");
        return false;
    }
}



