function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classList.remove("form__message--succes", "form__message--succes");
    messageElement.classList.add('form__message--${type}');
}

function setInputError(inputElement, message) {
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector("form__input-error-message").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const forgotPasswordForm = document.querySelector("#forgotPassword");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkForgotPassword").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        forgotPasswordForm.classList.remove("form--hidden");
    });

    document.querySelector("#linkCreateAccount").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.add("form--hidden");
        createAccountForm.classList.remove("form--hidden");
    });

    document.querySelector("#linkLogin1").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.remove("form--hidden");
        createAccountForm.classList.add("form--hidden");
    });

    document.querySelector("#linkLogin2").addEventListener("click", e => {
        e.preventDefault();
        loginForm.classList.remove("form--hidden");
        forgotPasswordForm.classList.add("form--hidden");
    });

    loginForm.addEventListener("submit", e => {
        e.preventDefault();

        // Perform your AJAX/Fetc login

        setFormMessage(loginForm, "error", "Onjuiste gebruikersnaam en/of wachtwoord combinatie");
    });

    forgotPasswordForm.addEventListener("submit", e => {
        e.preventDefault();

        // Perform your AJAX/Fetc login

        setFormMessage(forgotPasswordForm, "error", "Geen email adres opgegeven");
    });


    document.querySelectorAll(".form__input").forEach(inputElement => {
        inputElement.addEventListener("blur", e => {
            if (e.target.id === "signupUsername" && e.target.value.length > 0 && e.target.value.length < 2) {
                setInputError(inputElement, "Gebruikersnaam moet tenminste 2 tekens bevatten.");
            }
        });

        inputElement.addEventListener("input", e => {
            clearInputError(inputElement);
        });      
    });
});
