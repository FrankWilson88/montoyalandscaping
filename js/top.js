var up = document.getElementById('top');
var width = window.innerWidth || document.body.clientWidth || document.documentElement.clientWidth;
var scroll = document.body.scrollTop || document.documentElement.scrollTop;
window.onscroll = function(){scrollFunction()};
function scrollFunction(){
  if(scroll > 50 && width < 500){
    up.style.display = "block";
  }
  else if (scroll < 1000 && width < 1200) {
    up.style.display = "block";
  }
  else{
    up.style.display = "none";
  }

}
function backToTop(){
  document.body.scrollTop = 1000;
  document.documentElement.scrollTop = 1000;
}
console.log("Top Feature is loaded");
