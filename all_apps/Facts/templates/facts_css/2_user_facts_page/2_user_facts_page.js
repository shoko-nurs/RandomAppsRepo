
    const token_test = document.currentScript.getAttribute('token_test')
    const delete_fact_fetch = document.currentScript.getAttribute('delete_fact_fetch')
    const get_first_facts = document.currentScript.getAttribute('get_first_facts')
    const add_fact_fetch = document.currentScript.getAttribute('add_fact_fetch')
    const edit_fact_fetch = document.currentScript.getAttribute('edit_fact_fetch')
    const add_category_fetch = document.currentScript.getAttribute('add_category_fetch')
    const get_facts_from_cat_fetch = document.currentScript.getAttribute('get_facts_from_cat_fetch')
    const edit_category_fetch = document.currentScript.getAttribute('edit_category_fetch')
    const user_categories_fetch = document.currentScript.getAttribute('user_categories_fetch')
    const api_key_fetch = document.currentScript.getAttribute('api_key_fetch')
    

    getCategories();
    GetSelectCategories();
    GetFirstFacts();




    function DeleteFactFetch(fact_id){
        url = delete_fact_fetch

        body = {
                "fact_id":fact_id,
                "api_key_fetch":api_key_fetch
            }


        // deletion requires csrf token.
        // we can also add csrf exempt option
        // making permission_classes=[] will not work here

        fetch(url,
                    {
                        method:"delete",
                        headers: {
                             'Content-type':'application/json',
                            'Accept': 'application/json',
                            'X-CSRFToken': token_test
                         },

                        body: JSON.stringify(body)

                    }

               


        )
        .then( (response)=> response.json())
        .then( function(data){

        
            }
        )


    }

    function GetFirstFacts(){
        url = get_first_facts

        fetch(url)
        .then((response)=> response.json())
        .then( function(data){
           
            if(data.message=="OK"){
               
            let count = 1

            for (let fact of data.data){

               let fact_item = `

                    <div class="line">

                        <div class="fact_name"  >
                
                            <span id=count_${count}>${count})</span> 
                            <span id=${fact.id} name=${fact.id}>${fact.fact}</span>
                
                        </div>
              
                        <div class='actions'>
                            <button id=edit_${fact.id}_btn>Edit</button>           
                                
                            <button id=delete_${fact.id}_btn>Delete</button>
                
                        </div>
        
                    </div>`
                    
                    document.getElementById('facts_list').insertAdjacentHTML('beforeend', fact_item)
                    count += 1;

                    let delete_fact_btn = document.getElementById(`delete_${fact.id}_btn`);

                    /////////////////////////////////// need to copy this ////////////////////////////
                    delete_fact_btn.addEventListener('click', function(){

                        DeleteFactFetch(`${fact.id}`);
                        GetFactsFromCategory();

                    })


                    let edit_fact_btn = document.getElementById(`edit_${fact.id}_btn`);
                    
                    edit_fact_btn.addEventListener('click', function(){
                    EditToSaveFact( `${fact.id}`,`edit_${fact.id}_btn` )

                    })
           
                
            }
        }

        })

    }
    
    

    
   

    document.getElementById('select_categories').addEventListener('change', function(){
        document.getElementById('facts_list').innerHTML=""
        GetFactsFromCategory();
    
    })






    async function GetSelectCategories(){
        let select_test_html = document.getElementById('select_categories_test');
        let select_html = document.getElementById('select_categories');
        select_html.innerHTML = ""
        select_test_html.innerHTML=`<option value="Random">Random</option>`
        let url =  `${user_categories_fetch}?api_key_fetch=${api_key_fetch}`


        fetch(url)
        .then((response)=>response.json())
        .then( function(data){

            for(let cat of data){

                let new_option = 
                `
                <option value="${cat.category}">${cat.category}</option>

                `
                select_html.innerHTML += new_option
                select_test_html.innerHTML += new_option
            }


        })

    }


    // Add new fact
    document.getElementById('add_fact_form').addEventListener('submit',
        function(e){
            e.preventDefault();
            let selected_category = document.getElementById('select_categories').value
            let new_fact = document.getElementById('add_fact_input').value;

            let body = {
                'new_fact':new_fact,
                'selected_category': selected_category,
                'api_key_fetch':api_key_fetch
            }

            if(new_fact!=""){
                
                url = add_fact_fetch
                
                fetch(url, 
                    {
                        method:"POST",
                        headers: {
                            'Content-type':'application/json',
                            'Accept': 'application/json',
                            'X-CSRFToken': token_test
                        },

                        body: JSON.stringify(body)

                    }
                )
                .then((response)=> response.json())
                .then(function(data){


                    if(data.message=="OK"){
                        console.log(123)
                        document.getElementById('facts_list').innerHTML = ""
                        console.log(456)
                        GetFactsFromCategory();
                        console.log(780)
                    }

                })
            
            }
        }
    )

    
  


    ///  Add new category
    document.getElementById('add_category_form').addEventListener('submit',

        function(e){ 
            e.preventDefault();

            let add_category_csrf = document.getElementById('add_category_csrf').value;
            let new_category = document.getElementById('add_category_input').value;
            let body = {
                'new_category':new_category,
                'api_key_fetch':api_key_fetch
            }
           

            if (new_category!=""){
                let url = add_category_fetch;

                fetch(url, 
                    {
                        method:"POST",
                        headers: {
                            'Content-type':'application/json',
                            'Accept': 'application/json',
                            'X-CSRFToken': add_category_csrf
                        },

                        body: JSON.stringify(body)

                    }
                
                
                )
                .then( (response)=>response.json())
                .then( function(data){

                    if(data.message=="OK"){

                        document.getElementById('categories_list').innerHTML = ""
                        getCategories();
                        GetSelectCategories();
                        GetFactsFromCategory();
                    }
                    
                    else{
                        alert(data.message)
                    }


                })
             
            
            }
            
        }
    
    )
    

    
    async function SaveFactFetch( input_id, old_fact){
        let input_line = document.getElementById(input_id);
        let edited_fact = input_line.value;                       

        url = edit_fact_fetch

        let body ={
                    'edited_fact':edited_fact,
                    'old_fact':old_fact,
                    'api_key_fetch':api_key_fetch
        }

        let f = await fetch(url,
            {
                method:"POST",
                headers: {
                            'Content-type':'application/json',
                            'Accept': 'application/json',
                            'X-CSRFToken': token_test
                        },
                
                body: JSON.stringify(body)

            }    
            

        )
        return await f.json()
    }


    async function SaveCatFetch(
                                input_id, 
                                old_cat_name, 
                                csrf_id,
                                ){


                
        let input_line = document.getElementById(input_id);
        let new_cat_name = input_line.value;
        let csrf = document.getElementById(csrf_id).value
        
        url = edit_category_fetch

        let body ={
                    'old_name':old_cat_name,
                    'new_name':new_cat_name,
                    'api_key_fetch':api_key_fetch
        }


        let r = await fetch(url,
        
            {
                method:'POST',
                headers: {
                            'Content-type':'application/json',
                            'Accept': 'application/json',
                            'X-CSRFToken': csrf
                        },
                
                body: JSON.stringify(body)
            }

        )

        return await r.json()
       

 
    }


    async function EditToSaveFact(span_id,edit_btn_id){
        let edit_btn = document.getElementById(edit_btn_id)
        let line = document.getElementById(span_id) 

        let new_input =
            `
            
                <input id="${span_id}_csrf" type="hidden" name="csrfmiddlewaretoken" value=${token_test}>
                <input id="${span_id}_input" 
                       name="${span_id}_input" 
                       type="text" 
                       value="${line.textContent}">
            
            `
        

        let new_form_element = document.createElement('form');
        new_form_element.innerHTML = new_input;
        line.replaceWith(new_form_element)

        let save_btn = document.createElement('button');
        save_btn.id = `"${span_id}_save_btn"`;
        save_btn.innerHTML = "Save";
        edit_btn.replaceWith(save_btn);

        save_btn.addEventListener('click', function(){

            SaveFactFetch(`${span_id}_input`, line.textContent)
            .then(function(response){

                let new_fact_text = response.message
                save_btn.replaceWith(edit_btn)
                new_form_element.replaceWith(line)
                line.textContent = new_fact_text
                document.getElementById('facts_list').innerHTML = ""
                GetFactsFromCategory()
            })

        })
    }

    async function EditToSave(line_id, edit_btn_id) {
        let edit_btn = document.getElementById(edit_btn_id)
        let line = document.getElementById(line_id)

        
        let new_input =
            `
            
                <input id="${line_id}_csrf" type="hidden" name="csrfmiddlewaretoken" value={{csrf_token}}>
                <input id="${line_id}_input" 
                       name="${line_id}_input" 
                       type="text" 
                       value="${line.textContent}">
            
            `
        
        let new_form_element = document.createElement('form');
        new_form_element.innerHTML = new_input;
        
        line.replaceWith(new_form_element)

        let save_btn = document.createElement('button');
        save_btn.id = `"${line_id}_save_btn"`;
        save_btn.innerHTML = "Save";

        edit_btn.replaceWith(save_btn);
        
        
        save_btn.addEventListener('click', function(){

            // let new_name_text = document.getElementById(`${line_id}_input`).value

            SaveCatFetch(`${line_id}_input`,line.textContent,`${line_id}_csrf`)
            .then( function(response){
                let new_name_text = response.message;
                          
                save_btn.replaceWith(edit_btn)
                new_form_element.replaceWith(line)
                line.textContent = new_name_text
                document.getElementById('select_categories').innerHTML=""
                GetSelectCategories()
            })


    })

}

    
    async function GetFactsFromCategory(){
        document.getElementById('facts_list').innerHTML=""
        let selected_category = document.getElementById('select_categories').value;
        
      
        url = `${get_facts_from_cat_fetch}?api_key_fetch=${api_key_fetch}&category=${selected_category}`

        fetch(url)
        .then((response)=>response.json())
        .then( function(data){
            
            if(data.message=="OK"){
               
            let count = 1

            for (let fact of data.data){

               let fact_item = `

                    <div class="line">

                        <div class="fact_name"  >
                
                            <span id=count_${count}>${count})</span> 
                            <span id=${fact.id} name=${fact.id}>${fact.fact}</span>
                
                        </div>
              
                        <div class='actions'>
                            <button id=edit_${fact.id}_btn>Edit</button>           
                                
                            <button id=delete_${fact.id}_btn>Delete</button>
                
                        </div>
        
                    </div>`
                    
                    document.getElementById('facts_list').insertAdjacentHTML('beforeend', fact_item)
                   
                    let delete_fact_btn = document.getElementById(`delete_${fact.id}_btn`);
                    delete_fact_btn.addEventListener('click', function(){

                        DeleteFactFetch(`${fact.id}`);
                        GetFactsFromCategory();
                    })

                    let edit_fact_btn = document.getElementById(`edit_${fact.id}_btn`);
                    
                    edit_fact_btn.addEventListener('click', function(){
                        EditToSaveFact( `${fact.id}`,`edit_${fact.id}_btn` )

                    })


                    

                    count += 1;
           
                
            }
        }

        })
    }

      
        
    




    async function getCategories() {
        
        

        let url = `${user_categories_fetch}?api_key_fetch=${api_key_fetch}`

        fetch(url)
            .then((response) => response.json())
            .then(function (data) {
                let count = 1;

                for (let cat of data) {
                    var cat_item = `

                    <div class="line">

                        <div class="category_name"  >
                
                            <span id=count_${count}>${count})</span> 
                            <span id=${cat.category} name=${cat.category}>${cat.category}</span>
                
                        </div>
              
                        <div class='actions'>
                            <button id=edit_${cat.category}_btn  >Edit</button>           
                                
                            <button id=delete_${cat.category}_btn>Delete</button>
                
                        </div>
        
                    </div>`

                    
                    document.getElementById('categories_list').insertAdjacentHTML('beforeend', cat_item)
                    count += 1;
                    
                    let delete_category_btn = document.getElementById(`delete_${cat.category}_btn`);
                    
                    // make deletion of the category function here
                    
                    let edit_btn = document.getElementById(`edit_${cat.category}_btn`);
                    
                    edit_btn.addEventListener('click', function(){

                        EditToSave( `${cat.category}`,`edit_${cat.category}_btn` )

                    })

                    

                }

            })

    }









