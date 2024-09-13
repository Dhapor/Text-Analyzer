from django.urls import path # type: ignore 
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # For the input form
    path('counter/', views.counter, name='counter'),  # For processing the form data
]


