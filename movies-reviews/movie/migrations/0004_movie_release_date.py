# Generated by Django 4.0.3 on 2024-05-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
