from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from appSkills.forms import addSkillForm
from .models import Skill

# Create your views here.
def skills(request):
    skills = Skill.objects.all()
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
            form.save()
            return HttpResponseRedirect(reverse('skills'))
        else:
            print(form.errors)
    else:
        form = addSkillForm()
                
    context = {'form': form}
    return render(request, 'appSkills/addSkill.html', context)
