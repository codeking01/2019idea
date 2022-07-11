import xadmin

# Create your models here.
from .models import CourseInfo, LessonInfo, VideoInfo, SourceInfo


# Create your models here.
class CourseInfoXadmin(object):
    list_display = ['image', 'name', 'study_time', 'study_time', 'lever', 'love_num', 'click_num', 'desc', 'detail',
                    'category', 'course_notice', 'course_need', 'teacher_tell', 'orginfo', 'teacherinfo', 'add_time']
    list_filter = ['name', 'lever']


class LessonInfoXadmin(object):
    list_display = ['name', 'courseinfo', 'add_time']


class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'url', 'lessoninfo', 'add_time']


class SourceInfoXadmin(object):
    list_display = ['name', 'down_load', 'courseinfo', 'add_time']


# 注册一下
xadmin.site.register(CourseInfo, CourseInfoXadmin)
xadmin.site.register(LessonInfo, LessonInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)
