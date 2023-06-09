# Generated by Django 4.1.7 on 2023-03-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datebase', '0003_artikles_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=20, verbose_name='Название услуги')),
                ('name', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('coment', models.TextField(max_length=200, verbose_name='Отзыв')),
                ('estimation', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AlterField(
            model_name='artikles',
            name='prise',
            field=models.CharField(max_length=10, verbose_name='цена'),
        ),
    ]
