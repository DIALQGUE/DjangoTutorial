from rest_framework import serializers
from .models import Skill, SkillExample

class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('__all__')

class exampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillExample
        fields = ('__all__')