# Generated by Django 4.0.5 on 2022-06-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSkills', '0007_alter_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
