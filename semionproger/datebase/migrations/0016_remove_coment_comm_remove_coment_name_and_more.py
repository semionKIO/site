# Generated by Django 4.1.7 on 2023-04-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datebase', '0015_delete_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coment',
            name='comm',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='service',
        ),
        migrations.AddField(
            model_name='coment',
            name='favorite_fruit',
            field=models.CharField(max_length=50, null=True, verbose_name='Ваш коментарий'),
        ),
    ]
