const profileBtn = document.querySelector("#user-menu-button");
const hamBtn = document.querySelector("#ham-btn");
const home = document.querySelectorAll(".home");
const projects = document.querySelectorAll(".projects");
const experience = document.querySelectorAll(".experience");
const about = document.querySelectorAll(".about");
const projectEdit = document.querySelector(".project-edit");
const closeModalBtn= document.querySelector('.close-modal')


function menuBackgroundColor() {
  const home = document.querySelector(".home");
  const projects = document.querySelector(".projects");
  const experience = document.querySelector(".experience");
  const skills = document.querySelector(".skills");

  switch (window.location.pathname) {
    case "/dashboard":
      home.classList.add("bg-gray-900");
      break;
    case "/project":
      projects.classList.add("bg-gray-900");
      break;
    case "/experience":
      experience.classList.add("bg-gray-900");
      break;
    case "/skills":
      skills.classList.add("bg-gray-900");
      break;
  }
}

document.addEventListener("DOMContentLoaded", menuBackgroundColor);

function profileOptionsDisplay() {
  const profileOptions = document.querySelector("#profile-options");
  profileOptions.classList.toggle("invisible");
}
function mobileMenuOptionDisplay() {
  const mobileMenu = document.querySelector("#mobile-menu");
  mobileMenu.classList.toggle("hidden");
}
function modalopen() {
  const modal = document.querySelector(".project-modal");
  modal.classList.remove("invisible");
}
function modalclose(){
    const modal = document.querySelector(".project-modal");
    modal.classList.add("invisible");
}

profileBtn.addEventListener("click", profileOptionsDisplay);
hamBtn.addEventListener("click", mobileMenuOptionDisplay);
projectEdit.addEventListener("click", modalopen);
closeModalBtn.addEventListener("click", modalclose)

