const manage_api_key_url = document.currentScript.getAttribute('manage_api_key_url');



async function ManageKey(){
    url = manage_api_key_url;

        fetch(url)
            .then((response) => response.json())
            .then(function (data) {

                document.querySelector('.key_display').innerHTML = data.data


            })

}

document.getElementById('manage_button').addEventListener('click', function (){


         if (document.getElementById('manage_button').innerHTML=="Claim"){

            ManageKey();
            document.querySelector('.description').innerHTML = "Your API key is";
            document.getElementById('manage_button').innerHTML = "Reset";
            document.querySelector('.to_doc').style.visibility = 'visible';
        }

        else{
             
            if(confirm("Reset API key")){

                ManageKey();
            }

        }
    }
)

document.getElementById