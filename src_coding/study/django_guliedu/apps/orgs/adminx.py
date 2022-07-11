import xadmin

# Create your models here.
from .models import CityInfo,OrgInfo,TeacherInfo


class CityInfoXadmin(object):
    list_display=['name','add_time']
    # model_icon='fa fa-user' #修改菜单栏主通的样式 这个是一个第三方的类
    model_icon='fa fa-map-marker'



class OrgInfoXadmin(object):
    list_display=['image','name','course_num','study_num','address','love_num','click_num','category','cityinfo','add_time']
    model_icon='fa fa-simplybuilt'


class TeacherInfoXadmin(object):
    list_display=['image','name','work_year','work_position','work_style','work_company','age','gender','love_num','click_num']
    model_icon='fa fa-user'

# 注册一下
xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(TeacherInfo,TeacherInfoXadmin)