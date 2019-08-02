"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import handler404, handler500
# 处理静态文件
from django.conf import settings
from django.views.static import serve
import re

# 导入的根路径是项目的根目录
from app01 import views

urlpatterns = [
    # 'demo/' => re.match(r'^admin/', 'demo/')
    url(r'^admin/', admin.site.urls),
    # 'demo/' => re.match(r'demo/','demo/')
    # 'demo/js/bootstrap.min.js'
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^demo_form/$', views.demo_form),
    url(r'^demo_form2/$', views.demo_form2),
    url(r'^demo_form_db/$', views.demo_form_db),
    # url包含
    url(r'^route_base/', include('apps.route_base.urls',namespace='route_base')),
    url(r'^route_resolve/', include('apps.route_resolve.urls', namespace='route_resolve')),
    url(r'^django_templates/',include('apps.django_templates.urls',namespace='django_templates')),
    url(r'^forms_base/', include('apps.forms_base.urls', namespace='forms_base')),
    url(r'^forms_auth/', include('apps.forms_auth.urls', namespace='forms_auth')),
    url(r'^django_view/', include('apps.django_view.urls', namespace='django_view')),
    # 自己添加规则来处理静态文件
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, {"document_root": settings.STATIC_ROOT}),
    # url(f'^href/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),
]

print(settings.STATIC_URL, settings.STATIC_ROOT)
handler404 = views.my404
handler500 = views.my500


