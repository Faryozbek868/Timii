from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('teachers/', views.teachers, name='teachers'),
    path('locations/', views.locations, name='locations'),
    path('contact/', views.contact, name='contact'),
]
