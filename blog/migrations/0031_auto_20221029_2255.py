# Generated by Django 3.2.7 on 2022-10-29 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20221029_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_category',
            name='text',
        ),
        migrations.RemoveField(
            model_name='game_category',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='game_category',
            name='youtube',
        ),
    ]