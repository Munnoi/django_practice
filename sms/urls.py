from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("add/", views.Add.as_view(), name="add"),
    path("edit/<int:pk>/", views.Edit.as_view(), name="edit"),
    path("delete/<int:pk>/", views.Delete.as_view(), name="delete"),
]