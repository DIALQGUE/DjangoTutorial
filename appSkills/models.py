from django.db import models

# Create your models here.

class Skill(models.Model):
    LEVEL = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('practical', 'Practical'),
        ('advanced', 'Advanced'),
        ('professional', 'Professional')
    ]
    
    title = models.CharField(max_length = 60)
    level = models.CharField(max_length = 20, choices = LEVEL)
    example = models.CharField(max_length = 150, null = True)