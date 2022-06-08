from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from .api_views import router
from django.urls import path, include

from appSkills import api_views

urlpatterns = [
    path('', views.skills, name = 'skills'),
    path('<int:skillID>', views.skill, name = 'skill'),
    path('add', views.addSkill, name = 'addSkill'),
    path('<int:skillID>/delete', views.deleteSkill, name = 'deleteSkill'),
    path('<int:skillID>/edit', views.editSkill, name = 'editSkill'),
    path('api', include(router.urls), name = 'apiSkill'),
]