"""
@file:   urls.py
@author: Liu
@date:   2019/08/01
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view_test/', views.view_test, name="view_test"),
    url(r'^zoo/(\d+)/', views.zoos, name="zoos"),
    # 模板视图
    url(r'^templateview/$', views.MyTemplateView.as_view(), name="templatesview"),
    # 展示所有的用户信息到页面上
    url(r'^listview/$', views.MyListView.as_view(), name='listview'),
    # url(r'^listview/$', views.userinfo, name='listview'),
    url(r'^detailview/(?P<user_id>\d+)/$', views.MyDetailView.as_view(), name="detailview"),
    # url(r'^detailview/(\d+)/$', views.MyDetailView.as_view(), name="detailview"),
]