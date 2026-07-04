document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {

        const inputs = document.querySelectorAll("input");

        for(let input of inputs){

            if(input.value.trim()===""){

                alert("Please fill all fields.");

                event.preventDefault();

                return;
            }

            if(Number(input.value)<0){

                alert("Values cannot be negative.");

                event.preventDefault();

                return;
            }

        }

    });

});
