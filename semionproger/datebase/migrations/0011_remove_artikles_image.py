# Generated by Django 4.1.7 on 2023-03-29 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datebase', '0010_remove_coment_comm_artikles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikles',
            name='image',
        ),
    ]
