# Generated by Django 4.1.7 on 2023-04-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datebase', '0016_remove_coment_comm_remove_coment_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coment',
            old_name='favorite_fruit',
            new_name='comm',
        ),
        migrations.AddField(
            model_name='coment',
            name='fruit',
            field=models.CharField(max_length=50, null=True, verbose_name='ваш фрукт'),
        ),
        migrations.AddField(
            model_name='coment',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя клиента'),
        ),
        migrations.AddField(
            model_name='coment',
            name='service',
            field=models.CharField(max_length=20, null=True, verbose_name='Название услуги'),
        ),
    ]