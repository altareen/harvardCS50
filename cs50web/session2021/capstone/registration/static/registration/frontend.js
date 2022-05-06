document.addEventListener('DOMContentLoaded', function() {

});

function edit_description(id) {
    // Hide the edit button and clear out the description region
    document.querySelector(`#edit_description_${id}`).style.visibility = "hidden";
    let description = document.querySelector(`#description_${id}`).innerHTML;
    document.querySelector(`#description_${id}`).innerHTML = "";
    
    // Build up the text_area components one by one
    let update = document.createElement('div');
    update.innerHTML = `<textarea id = "text_${id}" placeholder="${description}" rows="10" cols="80"></textarea>`
    document.querySelector(`#description_${id}`).append(update);

    let save = document.createElement('button');
    save.classList.add('btn');
    save.classList.add('btn-sm');
    save.classList.add('btn-outline-primary');
    save.innerText = 'Save';
    document.querySelector(`#description_${id}`).append(save);
    
    let cancel = document.createElement('button');
    cancel.classList.add('btn');
    cancel.classList.add('btn-sm');
    cancel.classList.add('btn-outline-primary');
    cancel.innerText = 'Cancel';
    document.querySelector(`#description_${id}`).append(cancel);
    
    save.addEventListener("click", () => {
        let content = document.querySelector(`#text_${id}`).value;
        
        fetch('/update_description', {
            method: 'POST',
            body: JSON.stringify({
                course_id: id,
                submission: content
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            //console.log(result);
        });
        
        // Unhide the edit button and replace the course description region
        document.querySelector(`#edit_description_${id}`).style.visibility = "visible";
        document.querySelector(`#description_${id}`).innerHTML = content;
    });
    
    cancel.addEventListener("click", () => {
        // Unhide the edit button and replace the course description region
        document.querySelector(`#edit_description_${id}`).style.visibility = "visible";
        document.querySelector(`#description_${id}`).innerHTML = description;
    });
}


function edit_capacity(id) {
    // Hide the edit button and clear out the capacity region
    document.querySelector(`#edit_capacity_${id}`).style.visibility = "hidden";
    let quantity = document.querySelector('#quantity').innerHTML;
    let capacity = document.querySelector(`#capacity_${id}`).innerHTML;
    document.querySelector(`#capacity_${id}`).innerHTML = "";
    
    // Build up the input components one by one
    let update = document.createElement('span');
    update.innerHTML = `<input type="number" id="input_capacity_${id}" placeholder="${capacity}" min="${quantity}" max="30" size="2"></input>`
    document.querySelector(`#capacity_${id}`).append(update);

    let save = document.createElement('button');
    save.classList.add('btn');
    save.classList.add('btn-sm');
    save.classList.add('btn-outline-primary');
    save.innerText = 'Save';
    document.querySelector(`#capacity_${id}`).append(save);
    
    let cancel = document.createElement('button');
    cancel.classList.add('btn');
    cancel.classList.add('btn-sm');
    cancel.classList.add('btn-outline-primary');
    cancel.innerText = 'Cancel';
    document.querySelector(`#capacity_${id}`).append(cancel);
    
    save.addEventListener("click", () => {
        let content = document.querySelector(`#input_capacity_${id}`).value;
        
        fetch('/update_capacity', {
            method: 'POST',
            body: JSON.stringify({
                course_id: id,
                submission: content
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            //console.log(result);
        });
        
        // Unhide the edit button and replace the course description region
        document.querySelector(`#edit_capacity_${id}`).style.visibility = "visible";
        document.querySelector(`#capacity_${id}`).innerHTML = content;
    });
    
    cancel.addEventListener("click", () => {
        // Unhide the edit button and replace the course description region
        document.querySelector(`#edit_capacity_${id}`).style.visibility = "visible";
        document.querySelector(`#capacity_${id}`).innerHTML = capacity;
    });
}


function edit_section(id) {
    // Hide the edit button
    document.querySelector(`#edit_section_${id}`).style.visibility = "hidden";
    let section = document.querySelector(`#section_${id}`).innerHTML;
    
    // Build up the select components one by one
    let update = document.createElement('span');
    update.innerHTML = `<select class="form-select" id="select_section_${id}">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                        </select>`
    document.querySelector(`#section_${id}`).append(update);

    let save = document.createElement('button');
    save.classList.add('btn');
    save.classList.add('btn-sm');
    save.classList.add('btn-outline-primary');
    save.innerText = 'Save';
    document.querySelector(`#section_${id}`).append(save);
    
    let cancel = document.createElement('button');
    cancel.classList.add('btn');
    cancel.classList.add('btn-sm');
    cancel.classList.add('btn-outline-primary');
    cancel.innerText = 'Cancel';
    document.querySelector(`#section_${id}`).append(cancel);
    
    save.addEventListener("click", () => {
        let content = document.querySelector(`#select_section_${id}`).value;
        
        fetch('/update_section', {
            method: 'POST',
            body: JSON.stringify({
                course_id: id,
                submission: content
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            //console.log(result);
        });
        
        // Unhide the edit button and replace the course section region
        document.querySelector(`#edit_section_${id}`).style.visibility = "visible";
        document.querySelector(`#section_${id}`).innerHTML = content;
    });
    
    cancel.addEventListener("click", () => {
        // Unhide the edit button and replace the course section region
        document.querySelector(`#edit_section_${id}`).style.visibility = "visible";
        document.querySelector(`#section_${id}`).innerHTML = section;
    });
}


function edit_department(id) {
    // Hide the edit button
    document.querySelector(`#edit_department_${id}`).style.visibility = "hidden";
    let department = document.querySelector(`#department_${id}`).innerHTML;
    
    // Build up the select components one by one
    let update = document.createElement('span');
    update.innerHTML = `<select class="form-select" id="select_department_${id}">
                            <option value="Mathematics">Mathematics</option>
                            <option value="Science">Science</option>
                            <option value="Humanities">Humanities</option>
                            <option value="Languages">Languages</option>
                        </select>`
    document.querySelector(`#department_${id}`).append(update);

    let save = document.createElement('button');
    save.classList.add('btn');
    save.classList.add('btn-sm');
    save.classList.add('btn-outline-primary');
    save.innerText = 'Save';
    document.querySelector(`#department_${id}`).append(save);
    
    let cancel = document.createElement('button');
    cancel.classList.add('btn');
    cancel.classList.add('btn-sm');
    cancel.classList.add('btn-outline-primary');
    cancel.innerText = 'Cancel';
    document.querySelector(`#department_${id}`).append(cancel);
    
    save.addEventListener("click", () => {
        let content = document.querySelector(`#select_department_${id}`).value;
        
        fetch('/update_department', {
            method: 'POST',
            body: JSON.stringify({
                course_id: id,
                submission: content
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            //console.log(result);
        });
        
        // Unhide the edit button and replace the course department region
        document.querySelector(`#edit_department_${id}`).style.visibility = "visible";
        document.querySelector(`#department_${id}`).innerHTML = content;
    });
    
    cancel.addEventListener("click", () => {
        // Unhide the edit button and replace the course department region
        document.querySelector(`#edit_department_${id}`).style.visibility = "visible";
        document.querySelector(`#department_${id}`).innerHTML = department;
    });
}


function edit_title(id) {
    // Hide the edit button and clear out the title region
    document.querySelector(`#edit_title_${id}`).style.visibility = "hidden";
    let title = document.querySelector(`#title_${id}`).innerHTML;
    document.querySelector(`#title_${id}`).innerHTML = "";
    
    // Build up the input components one by one
    let update = document.createElement('span');
    update.innerHTML = `<input type="text" id="input_title_${id}" placeholder="${title}"></input>`
    document.querySelector(`#title_${id}`).append(update);

    let save = document.createElement('button');
    save.classList.add('btn');
    save.classList.add('btn-sm');
    save.classList.add('btn-outline-primary');
    save.innerText = 'Save';
    document.querySelector(`#title_${id}`).append(save);
    
    let cancel = document.createElement('button');
    cancel.classList.add('btn');
    cancel.classList.add('btn-sm');
    cancel.classList.add('btn-outline-primary');
    cancel.innerText = 'Cancel';
    document.querySelector(`#title_${id}`).append(cancel);
    
    save.addEventListener("click", () => {
        let content = document.querySelector(`#input_title_${id}`).value;
        
        fetch('/update_title', {
            method: 'POST',
            body: JSON.stringify({
                course_id: id,
                submission: content
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            //console.log(result);
        });
        
        // Unhide the edit button and replace the course title region
        document.querySelector(`#edit_title_${id}`).style.visibility = "visible";
        document.querySelector(`#title_${id}`).innerHTML = content;
    });
    
    cancel.addEventListener("click", () => {
        // Unhide the edit button and replace the course title region
        document.querySelector(`#edit_title_${id}`).style.visibility = "visible";
        document.querySelector(`#title_${id}`).innerHTML = title;
    });
}


function edit_name(id) {
    // Hide the edit button
    document.querySelector(`#edit_name_${id}`).style.visibility = "hidden";
    let name = document.querySelector(`#name_${id}`).innerHTML;
    
    // Build up the select components one by one
    let update = document.createElement('span');
    update.innerHTML = `<select class="form-select" id="select_name_${id}">
                            <option value="Albus Dumbledore">Albus Dumbledore</option>
                            <option value="Quirinus Quirrell">Quirinus Quirrell</option>
                            <option value="Rubeus Hagrid">Rubeus Hagrid</option>
                            <option value="Severus Snape">Severus Snape</option>
                            <option value="Remus Lupin">Remus Lupin</option>
                        </select>`
    document.querySelector(`#name_${id}`).append(update);

    let save = document.createElement('button');
    save.classList.add('btn');
    save.classList.add('btn-sm');
    save.classList.add('btn-outline-primary');
    save.innerText = 'Save';
    document.querySelector(`#name_${id}`).append(save);
    
    let cancel = document.createElement('button');
    cancel.classList.add('btn');
    cancel.classList.add('btn-sm');
    cancel.classList.add('btn-outline-primary');
    cancel.innerText = 'Cancel';
    document.querySelector(`#name_${id}`).append(cancel);
    
    save.addEventListener("click", () => {
        let content = document.querySelector(`#select_name_${id}`).value;
        
        fetch('/update_name', {
            method: 'POST',
            body: JSON.stringify({
                course_id: id,
                submission: content
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            //console.log(result);
        });
        
        // Unhide the edit button and replace the course name region
        document.querySelector(`#edit_name_${id}`).style.visibility = "visible";
        document.querySelector(`#name_${id}`).innerHTML = content;
    });
    
    cancel.addEventListener("click", () => {
        // Unhide the edit button and replace the course name region
        document.querySelector(`#edit_name_${id}`).style.visibility = "visible";
        document.querySelector(`#name_${id}`).innerHTML = name;
    });
}



