# Generated by Django 4.1.7 on 2023-03-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datebase', '0002_alter_artikles_options_artikles_prise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikles',
            name='image',
            field=models.ImageField(default=0, upload_to='', verbose_name='фото'),
            preserve_default=False,
        ),
    ]
