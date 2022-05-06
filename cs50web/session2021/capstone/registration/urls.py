from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("course/<int:course_id>", views.details, name="details"),
    path("user/<int:user_id>", views.profile, name="profile"),
    path("create", views.create, name="create"),
    path("section", views.section, name="section"),
    path("select", views.select, name="select"),
    path("success", views.success, name="success"),
    path("drop", views.drop, name="drop"),
    path("roster", views.roster, name="roster"),
    path("remove", views.remove, name="remove"),
    path("update_description", views.update_description, name="update_description"),
    path("update_capacity", views.update_capacity, name="update_capacity"),
    path("update_section", views.update_section, name="update_section"),
    path("update_department", views.update_department, name="update_department"),
    path("update_title", views.update_title, name="update_title"),
    path("update_name", views.update_name, name="update_name"),
]
