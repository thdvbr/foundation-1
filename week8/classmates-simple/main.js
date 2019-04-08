
document.addEventListener("DOMContentLoaded", function(){
//if we dont have DOM I cannot print ^

// make containers that gets input 
// console.log the names 

var name = document.getElementById("name");
var button = document.querySelector(".button");

// function that runs onClick > saves names and print 

button.addEventListener('click', printName);

function printName(){
    let names = document.createElement('p');
    names.textContent = name.value;
    document.body.appendChild(names);
}
// empty the input form and focus it 

});
