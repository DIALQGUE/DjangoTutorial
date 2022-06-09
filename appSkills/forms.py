from faulthandler import disable
from django import forms
from appSkills.models import Skill, SkillExample

class addSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        labels = {
            'title' : 'Title',
        }

    def __init__(self, *args, **kwargs):
        super(addSkillForm, self).__init__(*args, **kwargs)
        
    level = forms.ChoiceField(
        choices = Skill.LEVEL,
        required = True,
        label = "Level",
        widget = forms.RadioSelect
        )

class addSkillExampleForm(forms.ModelForm):
    class Meta:
        model = SkillExample
        fields = ['title', 'URLs', 'description']
        labels = {
            'title' : 'Example title',
            'URLs' : 'Example URLs',
            'description' : 'Example description',
        }

    def __init__(self, *args, **kwargs):
        super(addSkillExampleForm, self).__init__(*args, **kwargs)

addSkillExampleFormSet = forms.modelformset_factory(
    SkillExample,
    form = addSkillExampleForm,
    extra = 0,
)
