# Generated by Django 5.0.4 on 2024-04-17 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0010_background_name_alter_background_defects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='name',
            field=models.CharField(default='féru de science', max_length=50),
            preserve_default=False,
        ),
    ]