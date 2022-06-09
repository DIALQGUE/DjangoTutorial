from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from rest_framework import viewsets, routers

from appSkills.forms import addSkillForm, addSkillExampleFormSet
from .models import Skill, SkillExample
from .serializers import exampleSerializer, skillSerializer


# Create your views here.
def skills(request):
    skills = Skill.objects.order_by('id')
    context = {'skills':skills}
    return render(request, 'appSkills/Skills.html', context)

def skill(request, skillID):
    selected = None
    try:
        selected = Skill.objects.get(id = skillID);
    except:
        print('Skill not found')
    context = {'skill': selected, 'skillID': skillID}
    return render(request, 'appSkills/Skill.html', context)

def addSkill(request):
    if request.method == 'POST':
        skillForm = addSkillForm(request.POST)
        exampleFormSet = addSkillExampleFormSet(request.POST)
        if all([skillForm.is_valid(), exampleFormSet.is_valid()]):
            skillID = skillForm.save()
            examples = exampleFormSet.save(commit = False)
            for example in examples:
                example.skillID = skillID
                example.save()
            return HttpResponseRedirect(reverse('skills'))
        else:
            print(skillForm.errors)
            print(exampleFormSet.errors)
    else:
        skillForm = addSkillForm()
        exampleFormSet = addSkillExampleFormSet(queryset = SkillExample.objects.none())
                
    context = {
        'skillForm': skillForm,
        'exampleFormSet' : exampleFormSet
        }
    return render(request, 'appSkills/addSkill.html', context)

def editSkill(request, skillID):
    try:
        skill = Skill.objects.get(id = skillID)
    except:
        print('Skill not found')
        return render(request, 'appSkills/Skill.html', {'skill': None})

    exampleList = SkillExample.objects.filter(skillID = skill)

    if request.method == 'POST':
        skillForm = addSkillForm(request.POST, instance = skill)
        exampleFormSet = addSkillExampleFormSet(request.POST, queryset = exampleList)
        if all([skillForm.is_valid(), exampleFormSet.is_valid()]):
            skillID = skillForm.save()
            examples = exampleFormSet.save(commit = False)
            for example in examples:
                example.skillID = skillID
                example.save()
            return HttpResponseRedirect(reverse('skills'))
        else:
            print(skillForm.errors)
            print(exampleFormSet.errors)
    else:
        skillForm = addSkillForm(instance = skill)
        exampleFormSet = addSkillExampleFormSet(queryset = exampleList)

    context = {
        'skillForm': skillForm,
        'exampleFormSet': exampleFormSet,
        'skillID': skillID
        }
    return render(request, 'appSkills/editSkill.html', context)

def deleteSkill(request, skillID):
    try:
        skill = Skill.objects.get(id = skillID)
    except:
        print('Skill not found')
        return render(request, 'appSkills/Skill.html', {'skill': None})
    
    skill.delete()
    return HttpResponseRedirect(reverse('skills'))

# api views
class skillsList(viewsets.ModelViewSet):
    
    serializer_class = skillSerializer
    queryset = Skill.objects.order_by('id')

    filter_fields = (
        'level',
    )

class exampleList(viewsets.ModelViewSet):
    
    serializer_class = exampleSerializer
    queryset = SkillExample.objects.order_by('id')

    filter_fields = (
        'skillID',
    )

    ordering_fields = (
        'id',
        'skillID',
    )

router = routers.DefaultRouter()
router.register(r'skills', skillsList, 'skills')
router.register(r'examples', exampleList, 'examples')