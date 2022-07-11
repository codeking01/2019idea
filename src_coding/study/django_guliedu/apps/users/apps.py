from django.apps import AppConfig

# 在apps下面的文件下修改下面的verbose_name 可以修改显示的名字
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    #修改显示的名字
    verbose_name='用户模块'
