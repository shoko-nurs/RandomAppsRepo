

var url = document.currentScript.getAttribute('url');

const options = document.querySelector('#options');

const give = document.querySelector('#button_1');
const facts_display = document.querySelector('#facts-display');



function makeUrl(){

    let new_url = url+getSelectValue();
    return new_url;

}

function getSelectValue() {
    let selected = options.value;
    console.log(typeof(selected));
    return selected;
}

url = makeUrl();

console.log(url);



async function getFacts(url) {

    fetch(url)
        .then((response) => response.json())
        .then(function (data) {
            console.log(data);

            // let test = data[0];

            // facts_display.innerHTML = test.fact;

            for (let i in data) {

                var fact = `<div class="displayed-facts">

                        ${data[i].fact}

                        </div>`


                facts_display.innerHTML += fact;
            }
        })
}


give.addEventListener('click', () => {
    
    let a = getFacts(url);

})





