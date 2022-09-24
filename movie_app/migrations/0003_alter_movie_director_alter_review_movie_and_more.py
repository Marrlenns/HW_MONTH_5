# Generated by Django 4.1.1 on 2022-09-24 16:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_app.director', verbose_name='Режиссер:'),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie', verbose_name='Отзыв к фильму'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]