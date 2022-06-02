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
    example = models.CharField(max_length = 150, default = '', blank = True)
    description = models.CharField(max_length = 300, default = '', blank = True)