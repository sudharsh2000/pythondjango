# Generated by Django 3.2.4 on 2021-11-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technoapp', '0003_rename_name_mobiles_mobname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categ',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='categ',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='mobname',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
