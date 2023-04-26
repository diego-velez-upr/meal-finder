//Hamburger menu function
console.log("up and running...")
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

var selectedFilters = [];
var yes = "yes";


function buttonClick(name) {
    const button = document.getElementById(name);
        
    console.log('Button clicked!');
    console.log(button.id);
    console.log('in');

    if(button.classList.contains('active')){
        console.log('Deactivated...');
        button.classList.remove('active')
        for(var i = 0; i < selectedFilters.length; i++){ 

            if ( selectedFilters[i] === button.textContent.toLowerCase()) { 
                selectedFilters.splice(i, 1); 
            }
        }

    }else{
        console.log('Activated...');
        button.classList.add('active');
        selectedFilters.push(button.textContent.toLowerCase())
    }         
    console.log(selectedFilters.length)
  }


