from .models import *
from django import forms
from django.forms import ModelForm,TextInput
import sqlite3

db = sqlite3.connect("F:\питон\сайт на джанго\MyFerstSite\semionproger\db.sqlite3")
sq1 = db.cursor()
sq1.execute(f"SELECT service FROM datebase_artikles ")
m = sq1.fetchall()
le = len(m)
print(le)
list =[]
z = int(0)
my = ('a')
while z < le:
    sq1.execute(f"SELECT service FROM datebase_artikles ")
    x = sq1.fetchall()[z][0]
    new =(x,x)
    list.append(new)
    z += 1



FRUIT_CHOICES= [
    ('cantaloupe', 'a'),
    ('mango', 'a'),
    ('honeydew', 'a'),
    ]


class Comentform(ModelForm):
    class Meta:
        model = Coment
        fields = [ 'name', 'comm','service']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'}),

            "comm": TextInput(attrs ={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),
            'service':forms.Select(choices=list, attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость'
            })
        }


class LocationChoiceField(forms.Form):
    cat = forms.ModelChoiceField(queryset=Artikles.objects.all())

