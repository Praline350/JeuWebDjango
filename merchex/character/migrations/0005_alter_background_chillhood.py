# Generated by Django 5.0.4 on 2024-04-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_rename_childhood_background_character_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='chillhood',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
