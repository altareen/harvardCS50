import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.views.decorators.csrf import csrf_exempt

from .models import User, Department, Course

class CreateCourseForm(forms.Form):
    title = forms.CharField(label="Title")
    TEACHERS = (('Rubeus Hagrid', 'Rubeus Hagrid'), ('Albus Dumbledore', 'Albus Dumbledore'), ('Quirinus Quirrell', 'Quirinus Quirrell'), ('Severus Snape', 'Severus Snape'), ('Remus Lupin', 'Remus Lupin'), )
    instructor = forms.ChoiceField(label="Instructor", choices=TEACHERS)
    capacity = forms.IntegerField(label="Capacity")
    SECTIONS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), )
    section = forms.ChoiceField(label="Section", choices=SECTIONS)
    DEPARTMENTS = (('Mathematics', 'Mathematics'), ('Science', 'Science'), ('Humanities', 'Humanities'), ('Languages', 'Languages'), )
    department = forms.ChoiceField(label="Department", choices=DEPARTMENTS)
    description = forms.CharField(label="Description")

class CreateSectionForm(forms.Form):
    SECTIONS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), )
    section = forms.ChoiceField(label="Section", choices=SECTIONS)

# Create your views here.

def index(request):
    return render(request, "registration/index.html", {
        "math_courses": Course.objects.filter(department__name="Mathematics"),
        "science_courses": Course.objects.filter(department__name="Science"),
        "humanities_courses": Course.objects.filter(department__name="Humanities"),
        "languages_courses": Course.objects.filter(department__name="Languages")
    })


def create(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            instructor = form.cleaned_data["instructor"]
            capacity = int(form.cleaned_data["capacity"])
            section = int(form.cleaned_data["section"])
            department = form.cleaned_data["department"]
            description = form.cleaned_data["description"]
            
            # Create the relevant database objects and save them
            last_name = instructor.split()[1]
            user = User.objects.get(last_name=last_name)
            d = Department.objects.get(name=department)
            c = Course(title=title, instructor=user, capacity=capacity, section=section, department=d, description=description)
            c.save()
            
            # Redirect user to the Course Listings page
            return HttpResponseRedirect(reverse("index"))
        else:
            # If the form is invalid, re-render the page
            return render(request, "registration/create.html", {
                "form": CreateCourseForm()
            })

    return render(request, "registration/create.html", {
        "form": CreateCourseForm()
    })


def roster(request):
    return render(request, "registration/roster.html", {
        "faculty": User.objects.filter(is_staff=True).exclude(id=1),    # NOTE: This is a hack to exclude the superuser account
        "students": User.objects.filter(is_staff=False)
    })


def details(request, course_id):
    return render(request, "registration/details.html", {
        "course": Course.objects.get(id=course_id)
    })


def profile(request, user_id):
    person = User.objects.get(id=user_id)
    courses = None
    if person.is_staff:
        courses = Course.objects.filter(instructor=person)
    else:
        courses = Course.objects.filter(students__id=person.id).order_by('section')
    return render(request, "registration/profile.html", {
        "person": person,
        "courses": courses
    })


def section(request):
    if request.method == "POST":
        form = CreateSectionForm(request.POST)
        if form.is_valid():
            section = int(form.cleaned_data["section"])

            return render(request, "registration/select.html", {
                "section": section,
                "courses": Course.objects.filter(section=section)
            })
        else:
            # If the form is invalid, re-render the page
            return render(request, "registration/section.html", {
                "form": CreateSectionForm()
            })

    return render(request, "registration/section.html", {
        "form": CreateSectionForm()
    })


def select(request):
    if request.method == "POST":
        course_id = request.POST["course_id"]
        course = Course.objects.get(id=course_id)
        student = User.objects.get(id=request.user.id)
        # If the student is already enrolled in a course in that section, remove it
        courses = Course.objects.filter(students__id=request.user.id)
        for lesson in courses:
            if lesson.section == course.section:
                lesson.students.remove(student)
        course.students.add(student)
        
        # Redirect user to the success page
        return render(request, "registration/success.html", {
            "student": student,
            "action": "added",
            "course": course,

        })
        
    return render(request, "registration/section.html", {
        "form": CreateSectionForm()
    })


def drop(request):
    if request.method == "POST":
        course_id = request.POST["course_id"]
        course = Course.objects.get(id=course_id)
        student = User.objects.get(id=request.user.id)
        course.students.remove(student)
        
        # Redirect user to the success page
        return render(request, "registration/success.html", {
            "student": student,
            "action": "dropped",
            "course": course,

        })
        
    return render(request, "registration/drop.html", {
        "courses": Course.objects.filter(students__id=request.user.id)
    })


def success(request):
    return render(request, "registration/success.html")


def remove(request):
    if request.method == "POST":
        course_id = request.POST["course_id"]
        course = Course.objects.get(id=course_id)
        course.delete()
        instructor = User.objects.get(id=request.user.id)
        
        # Redirect user to the success page
        return render(request, "registration/success.html", {
            "instructor": instructor,
            "action": "deleted",
            "course": course,

        })
        
    return render(request, "registration/remove.html", {
        "courses": Course.objects.filter(instructor=User.objects.get(id=request.user.id))
    })


@csrf_exempt
def update_description(request):
    # Updating the content must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of submission
    data = json.loads(request.body)
    course_id = int(data.get("course_id", ""))
    description = data.get("submission", "")
    
    # Update the description of the course corresponding to course_id
    c = Course.objects.get(id=course_id)
    c.description = description
    c.save()

    return JsonResponse({"message": "Update sent successfully."}, status=201)


@csrf_exempt
def update_capacity(request):
    # Updating the content must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of submission
    data = json.loads(request.body)
    course_id = int(data.get("course_id", ""))
    capacity = int(data.get("submission", ""))
    
    # Retrive the object corresponding to course_id
    c = Course.objects.get(id=course_id)
    # Update the capacity of the course
    c.capacity = capacity
    c.save()

    return JsonResponse({"message": "Update sent successfully."}, status=201)


@csrf_exempt
def update_section(request):
    # Updating the content must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of submission
    data = json.loads(request.body)
    course_id = int(data.get("course_id", ""))
    section = int(data.get("submission", ""))
    
    # Retrive the object corresponding to course_id
    c = Course.objects.get(id=course_id)
    # Update the section of the course
    c.section = section
    c.save()

    return JsonResponse({"message": "Update sent successfully."}, status=201)


@csrf_exempt
def update_department(request):
    # Updating the content must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of submission
    data = json.loads(request.body)
    course_id = int(data.get("course_id", ""))
    department = data.get("submission", "")
    
    # Retrive the object corresponding to course_id
    c = Course.objects.get(id=course_id)
    # Update the department of the course
    d = Department.objects.get(name=department)
    c.department = d
    c.save()
    
    return JsonResponse({"message": "Update sent successfully."}, status=201)


@csrf_exempt
def update_title(request):
    # Updating the content must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of submission
    data = json.loads(request.body)
    course_id = int(data.get("course_id", ""))
    title = data.get("submission", "")
    
    # Retrive the object corresponding to course_id
    c = Course.objects.get(id=course_id)
    # Update the title of the course
    c.title = title
    c.save()

    return JsonResponse({"message": "Update sent successfully."}, status=201)


@csrf_exempt
def update_name(request):
    # Updating the content must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of submission
    data = json.loads(request.body)
    course_id = int(data.get("course_id", ""))
    instructor = data.get("submission", "")

    # Retrive the object corresponding to course_id
    c = Course.objects.get(id=course_id)
    # Retrieve the object corresponding to the instructor's last name
    last_name = instructor.split()[1]
    u = User.objects.get(last_name=last_name)
    # Update the instructor of the course
    c.instructor = u
    c.save()

    return JsonResponse({"message": "Update sent successfully."}, status=201)


#--------------------------------------
# Code snippets from CS50 Web
#--------------------------------------

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "registration/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        is_staff = request.POST.get("faculty", "") == "on"

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "registration/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = is_staff
            user.save()
            
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "registration/register.html")
