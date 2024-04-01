# The speach therapy center
The Speech Therapy Center is a comprehensive web application designed to facilitate seamless communication and management for both patients and staff in a speech therapy clinic located in the city of Blagoevgrad, Bulgaria. With a user-friendly interface, the platform offers various pages accessible both with and without login credentials, ensuring ease of access and functionality. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [User Management](#user-management)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)



## General Information
The Speech Therapy Center aims to address the challenges faced by speech therapy clinics in managing patient appointments, records, and communication between patients and staff. Traditional methods of managing appointments and patient records using paper-based systems or disparate digital tools can be inefficient and prone to errors. This application seeks to streamline these processes and enhance communication for improved patient care and administrative efficiency. 
The purpose of the Speech Therapy Center is to provide a centralized platform for patients to schedule appointments, monitor their progress, and communicate with their therapist. For staff members, the platform offers full patient information  and communicating with patients. By digitizing and centralizing these processes, the application aims to improve overall clinic efficiency and enhance the patient experience. 
The decision to undertake the development of the Speech Therapy Center was motivated by a recognition of the need for modernized and efficient management tools in speech therapy clinics. As the demand for speech therapy services continues to grow, there is a corresponding need for streamlined administrative processes and improved communication channels between patients and staff. By developing this application, I aim to contribute to the advancement of speech therapy services and the well-being of patients in our community.


## Technologies Used
- Django - version 4.0
- Python - version 3.10
- HTML5 
- CSS
- Java Script

## User Management
- User/Staff Registration: New users and staff can create accounts with unique emails and passwords.
- User/Staff Login: Registered users and staff can log in securely to access their profiles.


## Features
- Functionality without login credentials:
  - information about the center;
  - contact form and location information;
  - gallery.
- Functionality with login credentials:
     - for patients - Patients can update the profile information. They also can create, update, delete appointments (24h before the appointemnt patient can upate or delete the appointment). After each session they can fill or update patient diary with build in questionnaire and monitor their progress. Patient appointments are visible in the User diary section via dropbowns. 
     - for staff - Terapist can create, update, delete treatment plans,  view patient appointments and  profiles in the app.

## Screenshots
<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot1.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot2.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot4.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot5.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot6.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot7.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot8.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot9.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot10.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot11.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot12.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot13.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot14.jpg" />

<img align="center" width=480px  alt="home page view" src="https://github.com/vladodyanov/the_speach_therapy_center/blob/main/the_speach_therapy_center/staticfiles/img/screenshots/Screenshot15.jpg" />

## Setup
To set up the Speech Therapy Center locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/vladodyanov/the_speach_therapy_center.git
2. Navigate to the project directory:
-cd the_speach_therapy_center 
3. Install the required dependencies:
-pip install -r requirements.txt 
4. Apply migrations:
-python manage.py migrate 
5. Create a superuser to access the admin interface:
-python manage.py createsuperuser 
6. Run the development server:
-python manage.py runserver 
7. Access the application at http://localhost:8000 in your web browser.


## Usage
To use the Speech Therapy Center, follow these steps:
1. Register as a new user or log in if you already have an account.
2. Navigate through the different sections of the application, such as scheduling appointments, updating profile information, and viewing treatment plans.
3. Utilize the features available based on your role, whether you are a patient or a staff member.
4. Explore the various functionalities and interact with the interface to manage appointments and access patient information.

## Project Status
Project is: completed / under reiew

## Room for Improvement
To do:
- Install and setup Celery and Celery Beat to clean automatically  outdated appointments from the database .

## Contact
Created by Vladimir Dyanov - feel free to contact me!

