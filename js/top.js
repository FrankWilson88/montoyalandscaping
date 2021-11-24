var up = document.getElementById('top');
var width = window.innerWidth || document.body.clientWidth || document.documentElement.clientWidth;
var scroll = document.body.scrollTop || document.documentElement.scrollTop;
window.onscroll = function(){scrollFunction()};
function scrollFunction(){
  if (width < 500) {
    if(scroll > 50){
      up.style.display = "block";
    }
    else {
      up.style.display = "none";
    }
  }
  else {
    up.innerHTML = "shit";
  }
}
function backToTop(){
  document.body.scrollTop = 1000;
  document.documentElement.scrollTop = 1000;
}
console.log("Top Feature is loaded");
