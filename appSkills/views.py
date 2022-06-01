from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def skills(request):
    return HttpResponse('<h2>Skills</h2>')

def skill(request, skillID):
    return HttpResponse('Skill No.' + str(skillID))