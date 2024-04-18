# Generated by Django 5.0.4 on 2024-04-17 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_statmodifier_defect_skill_quality_skill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='stat_modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.statmodifier'),
        ),
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_skills', to='character.character')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_characters', to='character.skill')),
            ],
        ),
    ]