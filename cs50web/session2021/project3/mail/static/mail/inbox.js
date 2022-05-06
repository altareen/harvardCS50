document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');

    // Listen for submission of form
    document.querySelector('form').onsubmit = function() {
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: document.querySelector('#compose-recipients').value,
                subject: document.querySelector('#compose-subject').value,
                body: document.querySelector('#compose-body').value
            })
        })
        .then(response => response.json())
        .then(result => {
            // Print result
            console.log(result);
        });
        
        //load the sent mailbox
        load_mailbox('sent');
        
        // Stop form from submitting
        return false;
    }
});

function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#display-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
    
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#display-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // Send a GET request to retrieve all emails from the mailbox
    fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
        // Print emails
        //console.log(emails);

        // ... do something else with emails ...
        for (let i = 0; i < emails.length; i++) {
            const div = document.createElement('div');
            let shading = "";
            if (emails[i].read) {
                shading = `background-color: lightgray;`;
            }
            div.innerHTML = `<div style="border: 2px solid black; padding: 5px;` + shading + `">` +
                            `<strong>${emails[i].sender}</strong>
                             <span style="padding: 5px;">${emails[i].subject}</span>
                             <span style="color: gray; float: right;">${emails[i].timestamp}</span>
                             </div>`;
            div.addEventListener('click', function() {
                display_email(emails[i].id);
            });
            document.querySelector('#emails-view').append(div);
        }
    });
}


function display_email(id) {
    
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#display-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // Mark the specific email as read
    fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
        read: true
        })
    });

    // Send a GET request to retrieve the specific email from the mailbox
    fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
        // Print email
        //console.log(email);
        
        // Clear out the display-view region
        document.querySelector('#display-view').innerHTML = "";
        
        // Build up the display-view elements one by one
        let archive = document.createElement('div');
        let reply = document.createElement('button');
        reply.classList.add('btn');
        reply.classList.add('btn-sm');
        reply.classList.add('btn-outline-primary');
        reply.innerText = 'Reply';
        let body = document.createElement('div');

        // ... do something else with email ...
        let mode = "Archive";
        if (email.archived) {
            mode = "Unarchive";
        }
        archive.innerHTML = `<div><strong>From: </strong>${email.sender}</div>
            <div><strong>To: </strong>${email.recipients}</div>
            <div><strong>Subject: </strong>${email.subject}</div>
            <div><strong>Timestamp: </strong>${email.timestamp}</div>
            <button class="btn btn-sm btn-outline-primary" onclick="toggle_archive(${id}, ${email.archived})">` + mode + `</button>`;
        document.querySelector('#display-view').append(archive);
        
        reply.addEventListener("click", () => {
            console.log("You have clicked on Reply.");
            
            // Show compose view and hide other views
            document.querySelector('#emails-view').style.display = 'none';
            document.querySelector('#display-view').style.display = 'none';
            document.querySelector('#compose-view').style.display = 'block';

            // Pre-fill composition fields
            document.querySelector('#compose-recipients').value = email.sender;
            let prefix = email.subject.slice(0, 3);
            if (prefix != "Re:") {
                email.subject = "Re: " + email.subject;
            }
            document.querySelector('#compose-subject').value = email.subject;
            document.querySelector('#compose-body').value = email.body;
            document.querySelector('#compose-body').value = "On " + email.timestamp + " " + email.sender + " wrote:\n" + email.body;
        });

        document.querySelector('#display-view').append(reply);
        
        body.innerHTML = `<hr><div>${email.body}</div>`;
        document.querySelector('#display-view').append(body);
    });
}


function toggle_archive(id, flag) {

    // Toggle the specific email as archived/unarchived
    fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
        archived: !flag
        })
    });

    // Load the inbox
    window.location.reload();
}

