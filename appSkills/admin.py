from django.contrib import admin
from appSkills.models import Skill

class SkillAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'level', 'example', 'description']
    list_filter = ['level']
    
# Register your models here.
admin.site.register(Skill, SkillAdmin)