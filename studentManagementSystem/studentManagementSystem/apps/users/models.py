from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    The custom a user model on the basis of the original
    """
    mobile = models.CharField(max_length=11, unique=True, verbose_name='phone number')
    nickname = models.CharField(max_length=14, unique=True, verbose_name='nickname', default=None)
    gender = models.CharField(max_length=2, verbose_name='gender')
    header = models.ImageField(upload_to="studentManagementSystem/static/headers", default=None, null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
        verbose_name = 'userTable'
        verbose_name_plural = verbose_name