from django.contrib import admin
from appSkills.models import Skill, SkillExample

class ExampleInline(admin.StackedInline):
    model = SkillExample
    fields = [f.name for f in model._meta.fields]
    extra = 0

class SkillAdmin(admin.ModelAdmin):
    inlines = [ExampleInline]

    list_display = [f.name for f in Skill._meta.fields] + ['exampleSet']
    ordering = ['id']

    search_fields = ['title']
    list_filter = ['level']

    def get_queryset(self, request):
        queryset = super(SkillAdmin, self).get_queryset(request)
        return queryset

class ExampleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SkillExample._meta.fields]
    ordering = ['id']

    search_fields = ['skillID', 'exampleName']
    list_filter = ['skillID']

    raw_id_fields = ['skillID']
    
# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillExample, ExampleAdmin)