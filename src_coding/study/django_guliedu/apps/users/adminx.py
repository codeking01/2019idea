import xadmin
from .models import Bannerinfo,EmailVerifyCode
# 配置xadmim主题，注册的时候要用到专用的view去注册
from xadmin import views
class BaseXadminSetting(object):
    # 打开主题开发
    enable_themes = True
    #打开自带的主题
    use_bootswatch = True
# 设置全局外观
class CommXadminSetting(object):
    # 设置网站名字
    site_title='分布构效关系实验室管理系统'
    site_footer='XJL_exploit'
    #设置菜单样式 accordion不要写错了
    menu_style='accordion'


class BannerinfoXadmin(object):
    list_display=['image','url','add_time']
    # 加入搜索框
    search_fields=['code','email']
    #加入过滤器
    list_filter=['image','url']

class EmailVerifyCodeXadmin(object):
    list_display=['code','email','send_type','add_time']

# 2021年写好注册类以后发现再后台不显示，原来是django默认不显示 加入下面这个就解决了
hidden_menu = True
xadmin.site.register(Bannerinfo,BannerinfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
# 注册主题模块
xadmin.site.register(views.BaseAdminView,BaseXadminSetting)
# 注册全局样式类
xadmin.site.register(views.CommAdminView,CommXadminSetting)