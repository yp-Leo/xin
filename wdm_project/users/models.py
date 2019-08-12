from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_CHOICES = (
        ('1', '男'),
        ('0', '女'),
    )
    username = models.CharField(blank=True, null=True, max_length=20)
    password_hash = models.CharField(max_length=128, db_column='password')
    mobile = models.CharField(blank=True, null=True, max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    email = models.EmailField(null=True)



    def __str__(self):
        return self.username + "----" + self.password_hash

    class Meta:
        managed = False
        db_table = "v_user"

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = make_password(value)

    def check_pw(self, value):
        # 第一参数是未加密的原文
        # 第二个参数是加密后的秘文
        return check_password(value, self.password_hash)

    @classmethod
    def check_login(cls, username, password):
        # 按用户名查询
        user = cls.objects.filter(username=username).first()
        # 判定用户名是否正确，正确返回对象，否则None
        # if not user:
        #     return False
        # # 验证密码是否正确
        # if not check_password(password,user.password_hash):
        #     return False
        # return True
        return user and check_password(password,user.password_hash)



