from django.contrib import admin
from character.models import Character, Background, Skill
from character.models import Quality, Defect, CharacterSkill

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

admin.site.register(Character, CharacterAdmin)
admin.site.register(Background)
admin.site.register(Skill)
admin.site.register(Quality)
admin.site.register(Defect)
admin.site.register(CharacterSkill)

# Register your models here.
