from django.db import models


# Create your models here.


class Classroom(models.Model):
    c_name = models.CharField(max_length=255, default=None, unique=True)
    manager = models.CharField(max_length=66, default=None)
    Class_rating = models.CharField(max_length=3, default=None)
    # class_The_sorting = models.CharField(max_length=255, default=None)
    class_The_sorting = models.ForeignKey("TheSorting", models.CASCADE, related_name="classSorting", default=1)
    created = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.c_name

    class Meta:
        db_table = "db_class"
        verbose_name = "教室"
        verbose_name_plural = verbose_name


class Student(models.Model):
    join_school = models.DateTimeField(auto_now_add=True, verbose_name="join school date")
    name = models.CharField(max_length=4, default=None, verbose_name="name")
    gender = models.CharField(max_length=2, default=None)
    age = models.IntegerField(default=None)
    _class = models.CharField(max_length=55, default=None),
    address = models.CharField(max_length=255, default=None)
    belong_class = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="belong")
    idCart = models.CharField(max_length=99, default=None)
    header = models.ImageField(upload_to="studentManagementSystem/static/headers", default=None, null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "db_student"
        verbose_name = "student"
        verbose_name_plural = verbose_name


class Professional(models.Model):
    pro_name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.pro_name

    class Meta:
        db_table = "db_professional"
        verbose_name = "professional"
        verbose_name_plural = verbose_name


class Departments(models.Model):
    department = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.department

    class Meta:
        db_table = "db_depart"
        verbose_name = "departments"
        verbose_name_plural = verbose_name


class Coursera(models.Model):
    coursera_name = models.CharField(max_length=18, default=None)
    coursera_teacher = models.CharField(max_length=55, default=None)
    credit = models.IntegerField(default=5)
    coursera_comment = models.CharField(max_length=255, default=None)
    be_prs = models.ForeignKey(Departments, models.CASCADE, related_name="be_pr_for", default=1)
    probelong = models.ForeignKey(Professional, models.CASCADE, related_name='coursera_name')
    is_compulsory = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.coursera_name

    class Meta:
        db_table = "db_coursera"
        verbose_name = "coursera"
        verbose_name_plural = verbose_name


class Score(models.Model):
    grade = models.IntegerField(default=0)
    is_qualified = models.BooleanField(default=False)
    belong_student = models.ForeignKey(Student, models.CASCADE, related_name="belong_student", default=1)
    coursera_id = models.ForeignKey(Coursera, models.CASCADE, related_name="related_coursera")

    class Meta:
        db_table = "db_score"
        verbose_name = "score"
        verbose_name_plural = verbose_name


class TheSorting(models.Model):
    sortingName = models.CharField(max_length=255)
    def __str__(self):
        return self.sortingName

    class Meta:
        db_table = "db_sorting"
        verbose_name = "db_sorting"
        verbose_name_plural = verbose_name
