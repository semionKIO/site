from django.db import models
from django import forms
from django.shortcuts import render, redirect



class Artikles(models.Model):
    service = models.CharField('Название услуги', max_length=20, null=True)
    name = models.CharField('Имя сотрудника', max_length=250, null=True)
    info = models.TextField('Информация про услугу и сотрдника', max_length=250, null=True)
    prise = models.CharField('Цена', max_length=10, null=True)

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'




class Coment(models.Model):
    service = models.CharField('Название услуги', max_length=20, null=True)
    name = models.CharField('Имя клиента', max_length=20, null=True)
    comm = models.CharField('Ваш коментарий', max_length=50, null=True)

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'











