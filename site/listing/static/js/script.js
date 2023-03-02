/*  
File Name: script.js
*/

//Hamburger menu function
function menu() {
  var navlinks = document.getElementById("nav-links");
  var header = document.getElementById("mobilehead");
  var menuicon = document.getElementById("icon");
      if (navlinks.style.display === "block") {
          navlinks.style.display = "none";
          menuicon.style.color = "#f6eee4";
          header.style.color = "#f6eee4"
      }
       
      else {
          navlinks.style.display = "block";
          header.style.color = "#3c362d"
      }
}

 






 
