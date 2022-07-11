from datetime import datetime

from django.db import models

# Create your models here.
from users.models import UserProfile
from courses.models import CourseInfo


class UserAsk(models.Model):
    name = models.CharField(max_length=200, verbose_name="姓名")
    phone = models.CharField(max_length=11,default=0, verbose_name="联系电话")
    course = models.CharField(max_length=20, verbose_name="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "资讯信息"
        verbose_name_plural = verbose_name


class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile, verbose_name="收藏用户",on_delete=models.CASCADE)
    love_id = models.IntegerField(verbose_name="收藏id")
    love_type = models.IntegerField(choices=((1, 'org'), (2, 'course'), (3, 'teacher')), verbose_name="收藏类别")
    love_state = models.BooleanField(default=False, verbose_name="收藏状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name = "收藏信息"
        verbose_name_plural = verbose_name


# 用户课程类
class UserCourse(models.Model):
    # 把study_man和study_course改了
    study_man = models.ForeignKey(UserProfile, verbose_name="学习用户",on_delete=models.CASCADE)
    study_course = models.ForeignKey(CourseInfo, verbose_name="学习课程",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="学习时间")

    def __str__(self):
        return self.love_man.username

    class Meta:
        unique_together = ('study_man', 'study_course') #不允许 记录用户重复学习重复课程时间
        verbose_name = "用户学习课程信息"
        verbose_name_plural = verbose_name


class UserConmment(models.Model):
    comment_man = models.ForeignKey(UserProfile, verbose_name="评论用户",on_delete=models.CASCADE)
    comment_course = models.ForeignKey(CourseInfo, verbose_name="评论课程",on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=300, verbose_name="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

    def __str__(self):
        return self.comment_content

    class Meta:
        # unique_together = ('study_man', 'study_course') 忘记注释了
        verbose_name = "用户评论课程信息"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    # 如果是默认的id为0 ，那么则是系统消息，给每一个用户发消息，如果有id那就给指定的id的用户发消息
    message_user = models.IntegerField(default=0, verbose_name="消息用户")
    message_content = models.CharField(max_length=200, verbose_name="消息内容")
    message_status = models.BooleanField(default=False, verbose_name="消息状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    def __str__(self):
        return self.message_content

    class Meta:
        # unique_together = (('study_man','study_course'),) 忘记注释了
        verbose_name = "用户消息信息"
        verbose_name_plural = verbose_name
