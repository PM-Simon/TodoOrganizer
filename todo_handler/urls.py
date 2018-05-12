from django.urls import path, re_path
from todo_handler import views


urlpatterns = [
    path('', views.home, name = "index"),
    path('create', views.create, name = "create"),
    path('authors', views.authors, name = "authors"),
    path('removetodo/<int:pk>', views.remove_todo, name = "removetodo"),
    path('edit/<int:pk>', views.edit_todo, name = "edit"),
]