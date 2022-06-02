from asyncio.windows_events import NULL
from ftplib import all_errors
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Skill

allSkills = [
    {'id':4, 'title':'.NET', 'level':'beginner', 'example':'https://github.com/DIALQGUE/.Net-on-Microsoft-Learn'},
]

# Create your views here.
def skills(request):
    skills = Skill.objects.order_by('-level')
    context = {'skills':skills}
    return render(request, 'appSkills/Skills.html', context)

def skill(request, skillID):
    selected = None
    try:
        selected = Skill.objects.get(id = skillID);
    except:
        print('Skill not found')
    context = {'skill':selected}
    return render(request, 'appSkills/Skill.html', context)

    def addSkill(request):
        