# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 03:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('desc', models.CharField(max_length=300, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('detail', models.TextField(verbose_name='\u8bfe\u7a0b\u8be6\u60c5')),
                ('course_org', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u8bfe\u7a0b\u673a\u6784')),
                ('learn_times', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f\u6570)')),
                ('degree', models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u7ea7'), ('gj', '\u9ad8\u7ea7')], max_length=3, verbose_name='\u8bfe\u7a0b\u96be\u5ea6')),
                ('image', models.ImageField(max_length=300, upload_to='courses/%Y/m', verbose_name='\u5c01\u9762\u56fe')),
                ('students', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570')),
                ('click_num', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u4eba\u6570')),
                ('fav_num', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u8d44\u6e90\u540d\u79f0')),
                ('download', models.FileField(upload_to='courses/resource/%Y/%m', verbose_name='\u8d44\u6e90\u6587\u4ef6')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8d44\u6e90',
                'verbose_name_plural': '\u8bfe\u7a0b\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u7ae0\u8282\u540d\u79f0')),
                ('learn_time', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f\u6570)')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u7ae0\u8282',
                'verbose_name_plural': '\u8bfe\u7a0b\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u89c6\u9891\u540d\u79f0')),
                ('learn_time', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f(\u5206\u949f\u6570)')),
                ('url', models.CharField(max_length=100, verbose_name='\u8bbf\u95ee\u5730\u5740')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='\u7ae0\u8282')),
            ],
            options={
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
    ]
