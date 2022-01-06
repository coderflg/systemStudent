# -*- coding:utf-8 -*-
# @Time : 2021/11/26 15:23
# @Author : Sakura
# @QQEmail : 1018655370@qq.com
# @Google : jiangjiefeng0@gmail.com
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns = [
    url("^authorizations/$", views.UserLogin.as_view()),
    url("^register/$", views.UserRegister.as_view()),
    url("^check/(?P<pk>\d+)", views.Check.as_view())
]