
let button = document.querySelector(".button");
let display = document.querySelector(".par");
let facts = document.getElementById('js_script').getAttribute('facts');

console.log(button);
console.log(display);

button.addEventListener('click', ()=>{

    display.innerHTML = facts;



})