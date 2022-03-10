function validate()
{
    var signupUsername = document.getElementById("signupUsername").value;
    var signupPassword = document.getElementById("signupPassword").value;

    if(signupUsername=="admin"&& signupPassword=="admin123")
    {
        location.replace("UMCG_homepage.html");
        return false;
    }
}