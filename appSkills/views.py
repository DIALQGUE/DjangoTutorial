from django.shortcuts import render
from django.http.response import HttpResponse

all_skills = [
    {'id':1, 'title':'C/C++', 'level':'intermidiate', 'example':'https://github.com/DIALQGUE/Codeforce'},
    {'id':2, 'title':'Go', 'level':'beginner', 'example':'https://github.com/DIALQGUE/Lineman-Wongnai_Intern'},
    {'id':3, 'title':'JavaScript', 'level':'beginner', 'example':'https://github.com/Phyke/SleepyPoker'},
    {'id':4, 'title':'.NET', 'level':'beginner', 'example':'https://github.com/DIALQGUE/.Net-on-Microsoft-Learn'}
]

# Create your views here.
def skills(request):
    return render(request, 'appSkills/Skills.html')

def skill(request, skillID):
    return render(request, 'appSkills/Skill.html', context = {'skillID':skillID})