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

addSkillExampleFormSet = forms.modelformset_factory(
    model = SkillExample,
    fields = ['title', 'URLs', 'description'],
    labels = {
            'title' : 'Example title',
            'URLs' : 'Example URLs',
            'description' : 'Example Description'
        },
    extra = 0
)
