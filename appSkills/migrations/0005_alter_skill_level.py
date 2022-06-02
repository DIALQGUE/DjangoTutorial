# Generated by Django 4.0.5 on 2022-06-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSkills', '0004_alter_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[('beginner', 1), ('intermediate', 2), ('practical', 3), ('advanced', 4), ('professional', 5)], max_length=20),
        ),
    ]
