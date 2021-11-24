var vid = document.getElementById("vid");
var load = document.getElementById("load");
vid.onprogress = function(){load.innerHTML = "Loading..."};
vid.oncanplay = function(){load.innerHTML = "Loaded..."};
vid.oncanplaythrough = function(){load.innerHTML = ""};
