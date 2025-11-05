function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}
/* <!-- JavaScript for drag functionality -->*/
const waIcon = document.getElementById('wa-floating');

let isDragging = false;
let offsetX, offsetY;

waIcon.addEventListener('mousedown', (e) => {
  isDragging = true;
  offsetX = e.clientX - waIcon.getBoundingClientRect().left;
  offsetY = e.clientY - waIcon.getBoundingClientRect().top;
});

document.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  waIcon.style.left = `${e.clientX - offsetX}px`;
  waIcon.style.top = `${e.clientY - offsetY}px`;
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});
// No closing script tag needed in a JavaScript file
