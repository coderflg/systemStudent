# -*- coding:utf-8 -*-
# @Time : 2021/11/26 15:25
# @Author : Sakura
# @QQEmail : 1018655370@qq.com
# @Google : jiangjiefeng0@gmail.com
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # The custom register method
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = "__all__"


