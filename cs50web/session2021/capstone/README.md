# A Course Registration System

## Introduction
This capstone project implements a course registration system for the faculty and students of a fictional high school, namely, Hogwarts Academy. This website enables students to view the available course listings, add courses to their schedule, and drop them if necessary. The school's faculty has the ability to create new courses, make changes to an existing course listing, and delete a course.

## Distinctiveness and Complexity
This project satisfies the distinctiveness component, because I have had the opportunity to view many Learning Management Systems in this technology space, and none of them were able to implement a simple and effective scheduling system such as the one I have created here. I believe that this project is sufficiently complicated, because I had to code a significant amount of programming logic to deal with the inherent difficulties that this problem scope entails. For example, enforcing a capacity limit on the number of students that can be enrolled in a particular course was somewhat tricky to implement.

## Specification
This project is implemented mostly in Django, however, the section of the website where an instructor wishes to make changes to one of their courses, is done in JavaScript.

- **School Roster**: This displays a listing of all of the faculty and students present at Hogwarts Academy, separated into their respective groupings. Clicking on a name in the listing brings up that person's schedule.
- **View Schedule**: This presents an overview of all of the courses that associated with that particular user. If the user is an instructor, it shows all of the courses that they teach. If the user is a student, it displays all of the courses for which they are currently registered.
- **Create Course**: This allows an instructor to create a new course listing, in which they must fill in the various attributes associated with a course, such as title, capacity and description.
- **Delete Course**: This gives an instructor the opportunity to delete any of the courses that they teach, simply by selecting a course from a drop-down list.
- **Edit Course**: Clicking on a course name brings the user to a page which describes the course in much more detail. If the user happens to be the instructor of that particular course, then an `Edit` button will appear after each attribute. Clicking on an `Edit` button will allow the instructor to make a persistent change to the course, and this is achieved using JavaScript.
- **Add Course**: This feature allows a student to register for a particular course. The user is presented with a drop-down list that enables them to select a particular section, and once selected, another drop-down list appears which allows them to choose a particular course from that section. If a course's capacity is reached, then that course option is greyed out, and is not available for selection.
- **Drop Course**: All of the courses for which a student is currently registered are presented in a drop-down list. Selecting a course from that list will cause that student to be removed from that course's roster.

## A Description of the Contents of the Files Created for this Project
- `requirements.txt` This indicates that the `django-crispy-forms` package was used.
- `registration/static/registration/frontend.js` This contains the JavaScript code which enables an instructor to edit the details of a course.
- `registration/templates/registration/create.html` This displays an HTML form which enables an instructor to create a new course.
- `registration/templates/registration/details.html` This displays the details of the course. If the logged in user is the instructor of this course, `Edit` buttons appear which allow that user to alter the details of the course.
- `registration/templates/registration/drop.html` This displays an HTML form which enables a student to remove themselves from a course's registration.
- `registration/templates/registration/index.html` This displays all of the available courses, organized by academic department.
- `registration/templates/registration/layout.html` This HTML code links the bootstrap 5.0 library, and outlines the structure of the navigation menu.
- `registration/templates/registration/login.html` This enables a user to securely log in to the web application.
- `registration/templates/registration/profile.html` This displays the courses that a student is registered for, or that an instructor teaches.
- `registration/templates/registration/register.html` This displays an HTML form which allows a user to set up an account with this web application.
- `registration/templates/registration/remove.html` This displays an HTML form which enables a student to remove themselves from a course's registration.
- `registration/templates/registration/roster.html` This displays an HTML table of all of the faculty and students present at the school.
- `registration/templates/registration/section.html` This displays an HTML form which allows a student to select a particular section.
- `registration/templates/registration/select.html` This displays an HTML form which enables a student to choose a particular course.
- `registration/templates/registration/success.html` This displays a message to the student, indicating that adding or dropping a course was successful.

## Models Used in this Project
- `User`
- `Department`
  - `name`
- `Course`
  - `title`
  - `description`
  - `instructor`
  - `capacity`
  - `section`
  - `department`
  - `students`

## How to Run this Web Application
- Establish the database with the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
- Then, run the Django web application with the following command:
```
python manage.py runserver
```
- Note that there is no form-based mechanism in this web application to create a new Department. This must be done by a superuser in the Django administrator appliance, before any new Courses can be set up.

