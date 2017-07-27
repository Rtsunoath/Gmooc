# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市名')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')

    tag = models.CharField(max_length=10, default=u'全国知名', verbose_name=u'机构标签')
    category = models.CharField(max_length=6, choices=(('gx', u'高校'), ('pxjg', u'培训机构'), ('gr', u'个人')),
                                verbose_name=u'机构类别')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    courses = models.IntegerField(default=0, verbose_name=u'课程数')
    address = models.CharField(max_length=100, verbose_name=u'机构地址')
    logo = models.ImageField(max_length=100, upload_to='org/%Y/%m', verbose_name=u'logo')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    city = models.ForeignKey(CityDict, verbose_name=u'城市')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    work_year = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=100, verbose_name=u'就职公司')
    points = models.CharField(max_length=100, verbose_name=u'教学特点')
    image = models.ImageField(max_length=100, upload_to='teacher/%Y/%m', verbose_name=u'头像')
    age = models.IntegerField(default=18, verbose_name=u'年龄')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
