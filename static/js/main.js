document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".glass-navbar");

    if (!navbar) {
        return;
    }

    function handleNavbarShadow() {
        if (window.scrollY > 20) {
            navbar.classList.add("navbar-scrolled");
        } else {
            navbar.classList.remove("navbar-scrolled");
        }
    }

    handleNavbarShadow();
    window.addEventListener("scroll", handleNavbarShadow);
});
