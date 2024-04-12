from django.urls import path
from rectpatchantennapp import views

urlpatterns = [
    path("Optimizer", views.RandomForest, name="optimizer"),
]
