document.addEventListener("DOMContentLoaded", function () {
    const form_container = document.querySelector('.form_container')
    const inputs = form_container.querySelectorAll("input");
    inputs.forEach(input => {
        console.log(input)
        const inputElementId = input.id;
        console.log(inputElementId)
        const labelElement = document.querySelector(`label[for="${inputElementId}"]`)
        input.blur()
        labelElement.classList.remove('all-labels')
        if (!input.value) {
            labelElement.classList.add('onBlur')
            labelElement.classList.remove('onFocus')
        } else {
            labelElement.classList.add('onBlur')
            labelElement.classList.remove('onFocus')
        }
    });
    inputs.forEach((element) => {

        element.addEventListener('blur', (event) => {
            const inputElementId = event.currentTarget.id;
            const labelElement = document.querySelector(`label.${inputElementId
                }`);
            labelElement.classList.remove('all-labels');
            if (!event.currentTarget.value) {
                labelElement.classList.add('onBlur')
                labelElement.classList.remove('onFocus')
            }
        })
    })
    inputs.forEach((element) => {

        element.addEventListener('focus', (event) => {
            const inputElementId = event.currentTarget.id;
            const labelElement = document.querySelector(`label.${inputElementId
                }`)
            labelElement.classList.remove('all-labels')
            labelElement.classList.add('onFocus')
            labelElement.classList.remove('onBlur')
        })
    })
});

document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    const signInButton = document.getElementById("sign-in-switch");
    const registerButton = document.getElementById("register-switch");

    signInButton.addEventListener("click", function () {
        slider.style.left = signInButton.offsetLeft + "5px";
        setTimeout(() => {
            window.location.href = signInButton.getAttribute('data-url');
        }, 200)
    });

    registerButton.addEventListener("click", function () {
        slider.style.left = registerButton.offsetLeft + "px";
        setTimeout(() => {
            window.location.href = registerButton.getAttribute('data-url')
        }, 200);
    });

});



// document.addEventListener("DOMContentLoaded", function() {
//     const slider = document.querySelector(".slider");
//     const signInButton = document.getElementById("sign-in-switch");
//     const registerButton = document.getElementById("register-switch");
//     const formContainer = document.getElementById("form-container");

//     // Function to position the slider and load the form
//     function positionSliderAndLoadForm(button) {
//         const url = button.getAttribute("data-url");
//         slider.style.left = button.offsetLeft + "px";
//         setTimeout(() => {
//             loadForm(url);
//         }, 300); // Wait for the transition to complete before loading the form
//     }

//     // Check the current URL and position the slider accordingly
//     const currentPath = window.location.pathname;
//     if (currentPath.includes("login")) {
//         positionSliderAndLoadForm(signInButton);
//     } else if (currentPath.includes("signup")) {
//         positionSliderAndLoadForm(registerButton);
//     }

//     // Add click event listeners to the buttons
//     signInButton.addEventListener("click", function() {
//         history.pushState(null, "", signInButton.getAttribute("data-url"));
//         positionSliderAndLoadForm(signInButton);
//     });

//     registerButton.addEventListener("click", function() {
//         history.pushState(null, "", registerButton.getAttribute("data-url"));
//         positionSliderAndLoadForm(registerButton);
//     });
// });