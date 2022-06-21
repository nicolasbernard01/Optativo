from django.db import models


class Curso(models.Model):

    name = models.CharField('name',max_length=20)
    profesor = models.CharField('profesor',max_length=20)
    duration = models.CharField('duration',max_length=10)
    price = models.IntegerField('price $')


class Evento(models.Model):

    name = models.CharField('name',max_length=20)
    city = models.CharField('city',max_length=20)
    date = models.CharField('date',max_length=20)
