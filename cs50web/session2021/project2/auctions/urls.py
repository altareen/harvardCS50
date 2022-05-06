from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("success", views.success, name="success"),
    path("close", views.close, name="close"),
    path("reactivate", views.reactivate, name="reactivate"),
    path("comment", views.comment, name="comment"),
    path("<str:category>", views.display, name="display"),
    path("message", views.message, name="message")
]
