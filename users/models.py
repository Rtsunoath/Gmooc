# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default=u'', verbose_name=u'昵称')
    birday = models.DateField(max_length=20, null=True, blank=True, verbose_name=u'生日')
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name=u'性别')
    address = models.CharField(max_length=100, default=u'', verbose_name=u'地址')
    moblie = models.CharField(max_length=15, null=True, blank=True, verbose_name=u'手机号')
    images = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='image/default.png', verbose_name=u'头像')

    class Meta():
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.CharField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(max_length=30,
                                 choices=(("register", u"注册"), ("forget", u"忘记密码"), ("up_date_email", u"修改邮箱")),
                                 verbose_name=u"验证码类型")
    add_time = models.DateField(max_length=20, verbose_name=u"发送时间", default=datetime.now)

    class Meta():
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(max_length=100, upload_to='banner/%Y/m', verbose_name=u'轮播图')
    url = models.CharField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(max_length=10, default=100, verbose_name=u'顺序')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')
