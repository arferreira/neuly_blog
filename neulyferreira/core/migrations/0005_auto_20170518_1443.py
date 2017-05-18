# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_banner', models.ImageField(blank=True, null=True, upload_to='banner/images', verbose_name='Imagem de Início')),
            ],
            options={
                'verbose_name': 'Banner Início',
                'verbose_name_plural': 'Banner Início',
                'ordering': ['-title'],
            },
        ),
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=models.CharField(max_length=250, verbose_name='Resumo'),
        ),
    ]