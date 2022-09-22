from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма:')
    description = models.TextField(null=True, blank=True, verbose_name='Описание фильма:')
    duration = models.IntegerField(default=30)
    director = models.ForeignKey(to=Director, verbose_name='Режиссер:',
                                 related_name='movies', on_delete=models.SET_NULL,
                                 null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.director}"


class Review(models.Model):
    text = models.TextField("Ваш отзыв")
    movie = models.ForeignKey(to=Movie, verbose_name='Отзыв к фильму',
                              related_name='reviews', on_delete=models.SET_NULL,
                              null=True, blank=True)

    def __str__(self):
        return f"{self.movie}"
