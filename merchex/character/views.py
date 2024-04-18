from django.http import HttpResponse
from django.shortcuts import render
from character.models import Character


def hello(request):
    return HttpResponse("<h1>Page d'accueil!</h1>")


def characters_selection(request):
    character = Character.objects.all()
    return render(
        request, 'characters/characters_selection.html',
        {'characters': character}
        )
