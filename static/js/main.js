const burgermenu = document.getElementById('burger-menu');
const navmenu = document.getElementById('navbar');
burgermenu.addEventListener('click', () => {
  navmenu.classList.toggle('show');
  
});