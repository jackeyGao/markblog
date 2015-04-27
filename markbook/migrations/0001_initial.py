# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u65e5\u5fd7\u6807\u9898')),
                ('slug', models.CharField(max_length=45, verbose_name='\u65e5\u5fd7URL')),
                ('content', models.TextField(verbose_name='\u65e5\u5fd7\u5185\u5bb9')),
                ('is_reply', models.BooleanField(verbose_name='\u662f\u5426\u8bc4\u8bba')),
                ('is_valid', models.BooleanField(verbose_name='\u662f\u5426\u6709\u6548')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='BlogTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u6a21\u677f\u540d\u79f0')),
                ('content', models.TextField(verbose_name='\u6a21\u677f\u6784\u9020')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u7c7b\u76ee\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u7c7b\u76ee\u63cf\u8ff0')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u6807\u7b7e\u63cf\u8ff0')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(to='markbook.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='markbook.Tag'),
        ),
        migrations.AddField(
            model_name='blog',
            name='template',
            field=models.ForeignKey(to='markbook.BlogTemplate'),
        ),
    ]
