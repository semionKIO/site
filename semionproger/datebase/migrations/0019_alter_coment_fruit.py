# Generated by Django 4.1.7 on 2023-04-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datebase', '0018_alter_coment_fruit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='fruit',
            field=models.CharField(max_length=100, verbose_name='Стоимость услуги'),
        ),
    ]
