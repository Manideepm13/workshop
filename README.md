# Online Workshop Registration System

This project is a CLI-based registration system for online workshops. Users can sign up for events, view available workshops, and manage the workshops through CRUD operations. The project includes a basic front-end interface with HTML pages and a backend system using JSON to store workshop data.
Project Structure

Online_Workshop_Registration_System/

├── index.html

├── styles.css

├── register.html

├── success.html

├── workshops.json

└── README.md

File Descriptions
1. index.html

    Purpose: Displays a list of available workshops and provides a link to the registration page.
   
    Content: A simple homepage with workshop listings and a registration button.

3. styles.css

    Purpose: Provides styling for the HTML pages.
   
    Content: Basic CSS to style the layout of the website, including fonts, buttons, and overall page appearance.

4. register.html

    Purpose: A form where users can sign up for a workshop.
   
    Content: A form that collects user details (name, email, and selected workshop) and allows users to submit their registration.

5. success.html

    Purpose: Confirms successful registration.
   
    Content: Displays a confirmation message, including the details of the workshop the user signed up for.

7. workshops.json

    Purpose: Stores the workshop data.
   
    Content: A JSON file containing the workshop name, date, description, and other relevant details. This file is used to load available workshops and manage registration.

Project Workflow

    Home Page (index.html):
    
        Users visit the homepage to view a list of available workshops.
        
        A button on the homepage links to the registration page.

    Registration Page (register.html):
    
        Users fill out a registration form with their personal details and choose a workshop to sign up for.
        
        Once submitted, users are directed to a confirmation page.

    Confirmation Page (success.html):
        Displays a success message, confirming the user's registration for the selected workshop.

    Workshop Data (workshops.json):
    
        All workshop details (name, description, date) are stored in this file. The system uses this file to manage and update available workshops.

How to Use

    View Available Workshops: Open index.html in a browser to view the list of workshops.
    
    Register for a Workshop: Click on the "Register Now" button to go to the register.html page and fill out the form.
    
    Confirmation: After registration, the success.html page will confirm your sign-up.
