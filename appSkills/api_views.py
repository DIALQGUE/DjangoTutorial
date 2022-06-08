from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, routers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from appSkills.views import skill

from .models import Skill
from .serializers import skillSerializer

class skillsList(viewsets.ModelViewSet):

    serializer_class = skillSerializer
    queryset = Skill.objects.all()

    # def skills(self, request):
    #     queryset = Skill.objects.all()
    #     serializer = skillSerializer(skill, many = True)
    #     return Response(serializer.data)

    # def skill(self, request, pk = None):
    #     queryset = Skill.objects.all()
    #     skill = get_object_or_404(queryset, id = pk)
    #     serializer = skillSerializer(skill, many = False)
    #     return Response(serializer.data)


router = routers.DefaultRouter()
router.register(r'skills', skillsList, 'skills')