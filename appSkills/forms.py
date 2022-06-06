from django import forms
from appSkills.models import Skill

class addSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        labels = {
            'title' : 'Title',
            'example' : 'Example',
            'exampleName' : 'Example name',
            'description' : 'Description'
        }

    def __init__(self, *args, **kwargs):
        super(addSkillForm, self).__init__(*args, **kwargs)
        self.fields['example'].required = False
        self.fields['exampleName'].required = False
        self.fields['description'].required = False
        
    level = forms.ChoiceField(
        choices = Skill.LEVEL,
        required = True,
        label = "Level",
        widget = forms.RadioSelect
        )
