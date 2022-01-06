from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializer
from django.contrib.auth import login, logout
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
import math


# Create your views here.
# class Student(GenericAPIView):
class Student(GenericAPIView):

    queryset = models.Student.objects.filter(is_delete=False)
    serializer_class = serializer.StudentSerializer
    # 只有管理员才可以访问
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    # permission_classes = [IsAdminUser]
    def get(self, request):
        data = self.get_queryset()
        # data = models.Student.objects.all()
        count = math.ceil(data.count() / 8)
        page = PageNumberPagination()
        page.page_size = 2
        page.max_page_size = 10
        page.page_query_param = "page"
        page.page_size_query_param = "size"
        page_list = page.paginate_queryset(data, request, self)
        ser = self.get_serializer(page_list, many=True)
        # ser = serializer.StudentSerializer(page_list, many=True)
        return Response({
            "data": ser.data,
            "allCount": count
        })

    def put(self, requests):
        studentId = requests.query_params.get("studentId")
        student = self.get_queryset().get(id=studentId)
        ser = self.get_serializer(student)
        return Response(ser.data)

    def delete(self, requests):
        studentId = requests.query_params.get("id")
        try:
            student = self.get_queryset().get(id=studentId)
        except:
            return Response({
                "error": "用户不存在!"
            })
        student.is_delete = True
        student.save()
        return Response("success")

    def post(self, request):
        modifyData = request.data.get("form")
        print(modifyData)
        if modifyData.get("opType") == "modify":
            try:
                classBe = models.Classroom.objects.get(c_name=modifyData.get("_class"))
                modifyStudent = self.get_queryset().get(id=modifyData.get("id"))
            except:
                return Response("error")
            modifyStudent.join_school = modifyData.get("date")
            modifyStudent.name = modifyData.get("name")
            modifyStudent.gender = modifyData.get("gender")
            modifyStudent.age = modifyData.get("age")
            modifyStudent.address = modifyData.get("address")
            modifyStudent.belong_class_id = classBe
            modifyStudent.idCart = modifyData.get("idCart")
            modifyStudent.save()
            return Response("success")
        try:
            classBe = models.Classroom.objects.get(c_name=modifyData.get("_class"))
        except:
            return Response("error")
        models.Student.objects.create(
            join_school=modifyData.get("date"),
            name=modifyData.get("name"),
            gender=modifyData.get("gender"),
            age=modifyData.get("age"),
            address=modifyData.get("address"),
            belong_class=classBe,
            idCart=modifyData.get("idCart")
        ).save()
        return Response("success")


class ManagerDelete(GenericAPIView):
    queryset = models.Student.objects.filter(is_delete=True)
    serializer_class = serializer.StudentSerializer

    def get(self, requests):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)

    def put(self, requests):
        dele_id = requests.query_params.get("id")
        print(dele_id)
        try:
            stu = models.Student.objects.get(id=dele_id)
        except:
            return Response("error")
        stu.delete()
        return Response("success")

    def post(self, requests):
        deleteList = requests.data.get("list")
        try:
            for i in deleteList:
                ids = i["id"]
                models.Student.objects.get(id=ids).delete()
        except Exception as e:
            return Response({
                "error": e
            })
        return Response("success")

    def delete(self, requests):
        stuId = requests.query_params.get("id")
        try:
            stu = models.Student.objects.get(id=stuId)
        except:
            return Response("error")
        stu.is_delete = False
        stu.save()
        return Response("success")


class Classroom(GenericAPIView):
    queryset = models.Classroom.objects.filter(is_delete=False)
    serializer_class = serializer._ClassSerializer

    def get(self, request):
        data = self.get_queryset()
        count = math.ceil(data.count() / 7)
        page = PageNumberPagination()
        page.max_page_size = 8
        page.page_size = 2
        page.page_query_param = "page"
        page.page_size_query_param = "size"
        page_list = page.paginate_queryset(data, request, self)
        ser = self.get_serializer(page_list, many=True)
        return Response({
            "data": ser.data,
            "count": count
        })

    def put(self, request):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)

    def post(self, requests):
        data = requests.data.get("form")
        print(data.get("Class_rating"))
        print(data)
        if data.get("op") == "add":
            try:
                models.Classroom.objects.create(
                    c_name=data["c_name"],
                    manager=data["manager"],
                    Class_rating=data["Class_rating"],
                    class_The_sorting=models.TheSorting.objects.get(sortingName=data.get("class_The_sorting"))
                ).save()
            except Exception as e:
                print(e)
                return Response("failed")
            return Response("success")
        else:
            try:
                _class = models.Classroom.objects.get(id=data.get("id"))
            except Exception as e:
                print(e)
                return Response("failed")
            _class.c_name = data["c_name"]
            _class.manager = data["manager"]
            _class.Class_rating = data.get("Class_rating").strip()
            _class.class_The_sorting = models.TheSorting.objects.get(sortingName=data.get("class_The_sorting"))
            _class.save()
            return Response("success")

    def delete(self, requests):
        data = requests.query_params
        c_Id = data.get("id")
        if data.get("op") == "get":
            try:
                data = self.get_serializer(self.get_queryset().get(id=c_Id)).data
            except:
                Response("error")
            return Response(data)
        else:
            try:
                cls = self.get_queryset().get(id=c_Id)
            except:
                return Response('error')
            cls.is_delete = True
            cls.save()
            return Response("success")


class Coursera(GenericAPIView):
    queryset = models.Coursera.objects.filter(is_delete=False)
    serializer_class = serializer.CourseraSerializer

    def get(self, request):
        data = self.get_queryset()
        pageCount = data.count() / 7
        page = PageNumberPagination()
        page.page_size = 2
        page.max_page_size = 7
        page.page_query_param = "page"
        page.page_size_query_param = "size"
        pageList = page.paginate_queryset(data, request, self)
        ser = self.get_serializer(pageList, many=True)
        return Response({
            "data": ser.data,
            "pageCount": pageCount
        })

    def post(self, requests):
        data = requests.data.get("form")
        print(data)
        print(data.get("belong"))
        try:
            belong = models.Professional.objects.get(pro_name=data.get("classType"))
            be = models.Departments.objects.get(department=data.get("belong"))
        except Exception as e:
            print(e)
            return Response("error")
        if data.get("opTy") == "add":
            models.Coursera.objects.create(
                coursera_name=data.get("name"),
                coursera_teacher=data.get("teacher"),
                credit=data.get("credit"),
                coursera_comment=data.get("describe"),
                probelong=belong,
                be_prs=be,
                is_compulsory=data.get("compulsory")
            ).save()
            return Response("addSuccess")
        if data.get("opTy") == "modify":
            coursera = models.Coursera.objects.get(id=data.get("id"))
            coursera.coursera_teacher = data.get("teacher")
            coursera.coursera_name = data.get("name")
            coursera.credit = data.get("credit")
            coursera.probelong_id = belong
            coursera.be_prs = be
            coursera.coursera_comment = data.get("describe")
            coursera.is_compulsory = data.get("compulsory")
            coursera.save()
            return Response({
                "flag": "modifySuccess"
            })

    def delete(self, requests):
        return Response(serializer.ProSerializer(models.Professional.objects.all(), many=True).data)

    def put(self, requests):
        data = requests.query_params
        try:
            coursera = self.get_queryset().get(id=data.get("id"))
        except:
            return Response("error")
        ser = self.get_serializer(coursera)
        return Response(ser.data)


class Headers(APIView):
    def post(self, requests, pk):
        user = models.Student.objects.get(id=pk)
        data = requests.data["file"]
        user.header = data
        user.save()
        path = ""
        pathList = str(user.header).split("/")
        for index, item in enumerate(pathList):
            if index == 0:
                pass
            else:
                path += item + "/"
        print(path)
        return Response(path)


class CouseraManager(GenericAPIView):
    serializer_class = serializer.CourseraSerializer
    queryset = models.Coursera.objects.filter(is_delete=False)

    def get(self, requests):
        data = models.Departments.objects.all()
        ser = serializer.DepartmentsSerializer(data, many=True)
        return Response(ser.data)

    def delete(self, requests):
        deId = requests.query_params.get("id")
        try:
            c = models.Coursera.objects.get(id=deId)
            c.is_delete = True
        except:
            return Response("error")
        c.save()
        return Response("success")


class ManagerSorting(GenericAPIView):
    queryset = models.TheSorting.objects.all()
    serializer_class = serializer.SortingSerializer

    def get(self, requests):
        ser = self.get_serializer(self.get_queryset(), many=True)
        return Response(ser.data)
