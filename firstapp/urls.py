from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloIndia.as_view()),
    path('reservation', views.home)
]

#we need to map and connect the urls.py file from the app level to the project level so we will now go to the urls.py of the firstproject.