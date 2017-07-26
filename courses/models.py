# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'课程名称')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    course_org = models.CharField(max_length=50, verbose_name=u'课程机构', null=True, blank=True)

    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    degree = models.CharField(max_length=3, choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')), verbose_name=u'课程难度')
    image = models.ImageField(max_length=300, upload_to='courses/%Y/m', verbose_name=u'封面图')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击人数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏人数')

    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta():
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名称')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta():
        verbose_name = u'课程章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    url = models.CharField(max_length=100, verbose_name=u'访问地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta():
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'资源名称')
    download = models.FileField(max_length=100, upload_to='courses/resource/%Y/%m', verbose_name=u'资源文件')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta():
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name
