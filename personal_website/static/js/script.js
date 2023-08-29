
// goes to the corresponding section when clicked from navbar
// ex.) when you click About, it leads you to the about page
function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
  }

// Opens resume (Not used)
function openResume() {
    var resumeUrl = "{% static 'resume_website.pdf' %}";
    window.open(resumeUrl, '_blank');
}