# -*- coding:utf-8 -*-
# @Time : 2021/11/26 22:26
# @Author : Sakura
# @QQEmail : 1018655370@qq.com
# @Google : jiangjiefeng0@gmail.com
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class ScoreSerializer(ModelSerializer):
    coursera_id = serializers.StringRelatedField()

    class Meta:
        model = models.Score
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    belong_student = ScoreSerializer(many=True)
    belong_class = serializers.StringRelatedField()

    class Meta:
        model = models.Student
        fields = "__all__"


class _ClassSerializer(ModelSerializer):
    class_The_sorting = serializers.StringRelatedField()

    def create(self, validated_data):
        classroom = models.Classroom.objects.create(**validated_data)
        return classroom

    def update(self, instance, validated_data):
        print(validated_data)
        instance.c_name = validated_data["c_name"]
        instance.manager = validated_data["manager"]
        instance.Class_rating = validated_data["Class_rating"]
        instance.class_The_sorting = models.TheSorting.objects.get(sortingName=validated_data["class_The_sorting"])
        instance.save()
        return instance

    belong = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = models.Classroom
        fields = "__all__"


class DepartmentsSerializer(ModelSerializer):
    class Meta:
        model = models.Departments
        fields = "__all__"


class CourseraSerializer(ModelSerializer):
    probelong = serializers.StringRelatedField()
    be_prs = serializers.StringRelatedField()

    class Meta:
        model = models.Coursera
        fields = "__all__"


class ProSerializer(ModelSerializer):
    class Meta:
        model = models.Professional
        fields = "__all__"


class SortingSerializer(ModelSerializer):
    class Meta:
        model = models.TheSorting
        fields = "__all__"
