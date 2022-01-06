from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from student import serializer, models
import heapq
from django.http import FileResponse
import pandas as pd
from io import BytesIO

# Create your views here.

class StudentAnalysis(GenericAPIView):
    queryset = models.Classroom.objects.filter(is_delete=False)
    serializer_class = serializer._ClassSerializer

    def get(self, requests):
        global i
        query_class = requests.query_params.get("name")
        data = models.Classroom.objects.get(c_name=query_class)
        ser = self.get_serializer(data)
        # 提取课程名
        courseraName = [i['coursera_id'] for i in ser.data["belong"][0]["belong_student"]]
        # 获得学生字典并排序
        studentDict = []
        # 及格分数线
        rate = 100 * len(courseraName) * 0.6
        qualified = 0
        for i in ser.data["belong"]:
            temp = {}
            temp["name"] = i["name"]
            temp["total"] = 0
            tempList = []
            for j in i["belong_student"]:
                tempList.append(j["grade"])
                temp["total"] += j["grade"]
            if temp["total"] > rate:
                qualified += 1
            temp["score"] = tempList
            studentDict.append(temp)
        allCount = len(studentDict)
        orderData = sorted(studentDict, key=lambda x:x["total"], reverse=True)
        orderData = orderData[:5]
        qualified_rate = round(qualified / allCount, 2)
        studentName = [i["name"] for i in orderData]
        stu = {}
        for index, item in enumerate(orderData):
            stu["s%d"%index] = item["score"]
        res = [i["score"] for i in orderData]
        al = []
        try:
            al = list(map(lambda u, v, w, x, y: u + v + w + x + y, res[0], res[1], res[2], res[3], res[4]))
        except:
            pass
        return Response({
            "studentName": studentName,
            "courseraName": courseraName,
            "studentScore": orderData,
            "qualified": qualified_rate,
            "score": stu,
            "rate": al
        })
    def post(self, requests):
        data = requests.data
        flag = data.get("flag")
        if flag == "student":
            studentList = []
            student = models.Student.objects.filter(is_delete=False)
            ser = serializer.StudentSerializer(student, many=True)
            for i in ser.data:
                temp = {}
                temp["学号"] = i["id"]
                temp["姓名"] = i["name"]
                temp["班级"] = i["belong_class"]
                temp["入学日期"] = i["join_school"]
                temp["性别"] = i["gender"]
                temp["年龄"] = i["age"]
                temp["日期"] = i["address"]
                temp["身份证号"] = i["idCart"]
                studentList.append(temp)

            df = pd.DataFrame(studentList)
            df.to_excel("studentManagementSystem/static/data/" + flag + ".xlsx")
            print(df)
            return Response("static/data/" + flag + ".xlsx")
        if flag == "classroom":
            classList = []
            data = models.Classroom.objects.all()
            ser = serializer._ClassSerializer(data, many=True)
            for i in ser.data:
                temp = {}
                temp["班级名"] = i["c_name"]
                temp["直属分院"] = i["class_The_sorting"]
                temp["辅导员"] = i["manager"]
                temp["班级评级"] = i["Class_rating"]
                temp["创建时间"] = i["created"]
                classList.append(temp)
            df = pd.DataFrame(classList)
            df.to_excel("studentManagementSystem/static/data/" + flag + ".xlsx")
            return Response("static/data/" + flag + ".xlsx")
        return Response("error")
    def put(self, requests):
        name = requests.query_params.get("name")
        try:
            stu = models.Student.objects.filter(name__contains=name)
        except:
            return Response({
                "error": "err",
                "msg": "没有该学生"
            })
        ser = serializer.StudentSerializer(stu, many=True)
        return Response(ser.data)


