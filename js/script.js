const toggle = document.getElementById("toggle");
const status = document.getElementById("status");
const nameInput = document.getElementById("guestName");


toggle.addEventListener("click", () => {


    let name = nameInput.value.trim();


    if(name === ""){

        alert("Entre ton nom avant de confirmer");

        return;

    }


    toggle.classList.toggle("active");


    if(toggle.classList.contains("active")){


        status.textContent = "Présence confirmée ✓";


        console.log(name + " participe");


    } else {


        status.textContent = "Je participe";


    }


});
const particles = document.querySelector(".particles");
for(let i = 0; i < 20; i++){
let p = document.createElement("span");  


p.style.left = Math.random() * 100 + "%";  

p.style.animationDuration =  
(5 + Math.random() * 8) + "s";  


p.style.animationDelay =  
Math.random() * 5 + "s";  


particles.appendChild(p);  
}