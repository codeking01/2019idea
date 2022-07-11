from  datetime import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# verbose_name 就是在后台显示的时间
class UserProfile(AbstractUser):
    image=models.ImageField(upload_to='user/',max_length=200,verbose_name="用户头像",null=True,blank=True)
    nick_name=models.CharField(max_length=20,verbose_name="用户昵称",null=True,blank=True)
    birthday=models.DateTimeField(verbose_name="用户生日",null=True,blank=True)
    gender=models.CharField(choices=(('boy','男'),('girl','女')),max_length=20,verbose_name="用户性别",default='boy')
    address=models.CharField(max_length=200,verbose_name="用户地址",null=True,blank=True)
    phone=models.CharField(max_length=11,verbose_name="用户手机",null=True,blank=True)
    #判断是否激活
    # is_start=models
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    def __str__(self):
        return self.username #取任何一个字段

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

class Bannerinfo(models.Model):
    image=models.ImageField(upload_to='banner/',verbose_name="轮播图片",max_length=200)
    url=models.URLField(default='http://www.baidu.com',max_length=200,verbose_name="图片链接")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name="轮播图信息"
        verbose_name_plural=verbose_name

class EmailVerifyCode(models.Model):
    code=models.CharField(max_length=20,verbose_name="邮箱验证码")
    email=models.EmailField(max_length=200,verbose_name="验证码邮箱")
    send_type=models.IntegerField(choices=((1,'register'),(2,'forget'),(3,'change')),verbose_name="验证码类型")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name='验证码邮箱'
        verbose_name_plural=verbose_name









