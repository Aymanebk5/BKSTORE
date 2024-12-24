document.addEventListener("DOMContentLoaded", function () {
    // Menu mobile
    const menuIcon = document.querySelector(".menu-icon");
    const nav = document.querySelector("nav");
    menuIcon.addEventListener("click", function () {
        nav.classList.toggle("active");
    });
    
      // Gestion de formulaire pour la page Compte
    const loginForm = document.getElementById("LoginForm");
    const regForm = document.getElementById("RegForm");
    const indicator = document.getElementById("Indicator");
    document.getElementById("btn1").addEventListener("click", function () {
        regForm.style.transform = "translateX(300px)";
        loginForm.style.transform = "translateX(300px)";
        indicator.style.transform = "translateX(0)";
    });
    
    document.getElementById("btn2").addEventListener("click", function () {
        regForm.style.transform = "translateX(0)";
        loginForm.style.transform = "translateX(0)";
        indicator.style.transform = "translateX(100px)";
    });
    });