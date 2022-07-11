"""django_guliedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#  注意这个include函数是在django.urls这个下面的 别写错地方了
# 配置xadmin
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

from users.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^admin/',admin.sites.urls)
    # path('admin/', admin.site.urls), 10.21日根据xadmin安装文档修改
    path('xadmin/', xadmin.site.urls),

    path('users/', include(('users.urls',"users"),namespace='users')),
    path('courses/', include(('courses.urls',"courses"),namespace='courses')),
    path('orgs/', include(('orgs.urls',"orgs"),namespace='orgs')),
    path('operations/', include(('operations.urls',"operations"),namespace='operations')),
    path('',index,name='index')
    # path('admin/',admin.sites.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
