from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from appSkills.forms import addSkillForm
from .models import Skill

allSkills = [
    {'id':4, 'title':'.NET', 'level':'beginner', 'example':'https://github.com/DIALQGUE/.Net-on-Microsoft-Learn'},
]

# Create your views here.
def skills(request):
    skills = Skill.objects.order_by('-levelRank')
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
    if request.method == 'POST':
        form = addSkillForm(request.POST)
        if form.is_valid():
            if form.level == 'Beginner':
                form.levelRank = 1;
            elif form.level == 'Intermediate':
                form.levelRank = 2;
            elif form.level == 'Practical':
                form.levelRank = 3;
            elif form.level == 'Advanced':
                form.levelRank = 4;
            else:
                form.levelRank = 5;
            form.save()
            return HttpResponseRedirect(reverse('skills'))
    else:
        form = addSkillForm()
                
    context = {'form': form}
    return render(request, 'appSkills/addSkill.html', context)
