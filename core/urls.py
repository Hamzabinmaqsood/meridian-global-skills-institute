from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admissions/', views.admissions, name='admissions'),
    path('ielts/', views.ielts, name='ielts'),
    path('study-abroad/', views.study_abroad, name='study_abroad'),
    path('leadership-training/', views.leadership, name='leadership'),
]
