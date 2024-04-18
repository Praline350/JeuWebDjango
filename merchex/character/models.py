from django.db import models
import json

# Create your models here.



class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stat_modifiers = models.JSONField(default=list)  # Champ JSONField pour stocker les modificateurs de statistiques

    def apply_modifiers(self, character):
        # Parcourt les modificateurs de statistiques
        for modifier in self.stat_modifiers:
            stat_name = modifier['stat']
            modifier_amount = modifier['amount']
            # Applique le modificateur de statistique au personnage
            setattr(character, stat_name, getattr(character, stat_name) + modifier_amount)
        # Enregistre les modifications apportées aux statistiques du personnage
        character.save()

    def __str__(self):
        return self.name


class Defect(models.Model):
    name = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skill, related_name='defects',blank=True)

    def __str__(self):
        return self.name


class Quality(models.Model):
    name = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skill, related_name='qualities', blank=True)

    def __str__(self):
        return self.name


class Background(models.Model):
    name = models.CharField(max_length=50)
    chillhood = models.CharField(max_length=100, null=True)
    qualities = models.ManyToManyField(Quality, related_name='backgrounds', blank=True)
    defects = models.ManyToManyField(Defect, related_name='backgrounds',blank=True)
    # Les champs pour les différents aspects du background ici

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.fields.CharField(max_length=60)
    age = models.fields.IntegerField()
    level = models.fields.PositiveIntegerField()
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('U', 'Unknow'),
    )
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    physical = models.PositiveIntegerField()
    agility = models.PositiveIntegerField()
    comprehension = models.PositiveIntegerField()
    intuition = models.PositiveIntegerField()
    social = models.PositiveIntegerField()
    background = models.ManyToManyField(Background, related_name='background')

    def __str__(self):
        return self.name


class CharacterSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='to_characters')

    # Autres champs pour la relation entre le personnage et la compétence