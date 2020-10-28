const burgermenu = document.getElementById('burger-menu');
const navmenu = document.getElementById('navbar');
console.log("Im working")
burgermenu.addEventListener('click', () => {
  navmenu.classList.toggle('show');
  
});