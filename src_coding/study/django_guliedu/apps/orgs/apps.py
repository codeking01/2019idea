from django.apps import AppConfig


class OrgsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orgs'
    # verbose_name不要打错了
    verbose_name='机构模块'
