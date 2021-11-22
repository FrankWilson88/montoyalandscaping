var up = document.getElementById('top');
window.onscroll = function(){scrollFunction()};
function scrollFunction(){
  if(document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000){
    up.style.display = "block";
  } else {
    up.style.display = "none";
  }
}
function topFunction(){
  document.body.scrollTop = 1000;
  document.documentElement.scrollTop = 1000;
}
console.log("Top Feature is loaded");
