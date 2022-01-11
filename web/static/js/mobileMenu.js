var tabContent = document.getElementById("tabContent");
function mobileMenu(){
  if (tabContent.style.display == "block") {
    tabContent.style.display = "none";
  }
  else {
    tabContent.style.display = "block";
  }
}
console.log("Mobile Menu Feature is Loaded");
