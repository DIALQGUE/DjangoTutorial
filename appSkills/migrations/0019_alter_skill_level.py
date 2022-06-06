# Generated by Django 4.0.5 on 2022-06-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSkills', '0018_skill_levelrank_alter_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Practical', 'Practical'), ('Advanced', 'Advanced'), ('Professional', 'Professional')], max_length=20),
        ),
    ]
