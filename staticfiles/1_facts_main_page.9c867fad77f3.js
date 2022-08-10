
var base_url = document.currentScript.getAttribute('url');


const give = document.querySelector('#button_1');
const facts_display = document.querySelector('#facts-display');



function getSelectValue() { 
    let selected = document.querySelector('#options').value;
    
    return selected;
}


function makeUrl(){

    let new_url = base_url+"?category="+getSelectValue();
    return new_url;

}



async function getFacts(url) {
    facts_display.innerHTML = ""
    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
           
            let number = data.length;
            let index = Math.floor((Math.random()*number));
            
            let test = data[index];
            facts_display.innerHTML = test.fact;

            
        })
}


give.addEventListener('click', () => {
    let url_fetch = makeUrl();

    let a = getFacts(url_fetch);

})





