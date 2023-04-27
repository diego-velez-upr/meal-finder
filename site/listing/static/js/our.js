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

function buttonClick(name) {
    const button = document.getElementById(name);

    if (button.classList.contains('active')) {
        console.log('Removed ' + button.id + ' filter!');
        button.classList.remove('active')
        for(var i = 0; i < selectedFilters.length; i++){
            if ( selectedFilters[i] === button.textContent.toLowerCase()) { 
                selectedFilters.splice(i, 1); 
            }
        }
    } else {
        console.log('Applied ' + button.id + ' filter!');
        button.classList.add('active');
        selectedFilters.push(button.textContent.toLowerCase())
    }

    var xhr = new XMLHttpRequest();
    // Pass the selected filters to the python view updater
    xhr.open("GET", "apply_filters?filters=" + selectedFilters, true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onload = function() {
        // Received successful response
        if (xhr.status === 200) {
            // Get div where table of food goes
            var div = document.getElementById("listing-table");
            // Update food slots
            div.innerHTML = xhr.responseText;
        } else {
            console.log("Request failed. Returned status code: " + xhr.status);
        }
    };
    xhr.send();
  }


