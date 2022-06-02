from django.urls import path
from . import views

urlpatterns = [
    path('', views.skills, name = 'skills'),
    path('<int:skillID>', views.skill, name = 'skill'),
    path('add', views.addSkill, name = 'addSkill')
]