from django.test import TestCase
from .models import Character

# Create your tests here.

class CharacterModelTest(TestCase):
    character = Character.objects.first()

# Affiche tous les champs du personnage
    for field, value in character.__dict__.items():
        print(f"{field}: {value}")
    