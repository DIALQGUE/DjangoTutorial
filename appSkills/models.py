from django.db import models

# Create your models here.

class Skill(models.Model):
    LEVEL = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Practical', 'Practical'),
        ('Advanced', 'Advanced'),
        ('Professional', 'Professional')
    ]
    
    title = models.CharField(max_length = 20, unique = True)
    level = models.CharField(max_length = 20, choices = LEVEL)

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

    def example(self):
        exampleSet = SkillExample.objects.filter(skillID = self.id)
        if(exampleSet.__len__() > 0):
            return exampleSet
        return None

class SkillExample(models.Model):
    
    skillID = models.ForeignKey(Skill, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    URLs = models.CharField(max_length = 150)
    description = models.CharField(max_length = 300)

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)