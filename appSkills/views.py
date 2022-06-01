from asyncio.windows_events import NULL
from ftplib import all_errors
from django.shortcuts import render
from django.http.response import HttpResponse

allSkills = [
    {'id':1, 'title':'C/C++', 'level':'intermidiate', 'example':'https://github.com/DIALQGUE/Codeforce'},
    {'id':2, 'title':'Go', 'level':'beginner', 'example':'https://github.com/DIALQGUE/Lineman-Wongnai_Intern'},
    {'id':3, 'title':'JavaScript', 'level':'beginner', 'example':'https://github.com/Phyke/SleepyPoker'},
    {'id':4, 'title':'.NET', 'level':'beginner', 'example':'https://github.com/DIALQGUE/.Net-on-Microsoft-Learn'},
    {'id':5, 'title':'English', 'level':'practical', 'example': None}
]

# Create your views here.
def skills(request):
    context = {'skills':allSkills}
    return render(request, 'appSkills/Skills.html', context)

def skill(request, skillID):
    selected = None;
    try:
        selected = [f for f in allSkills if f['id'] == skillID][0]
    except IndexError:
        print('Outo of bound skill')
    context = {'skill':selected}
    return render(request, 'appSkills/Skill.html', context)