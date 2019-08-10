from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from users.models import User


def avatar_file_size(value):
    limit=2*1024*1024
    if value.size > limit:
        raise ValidationError('头像文件太大了，请限制在2M之内')

class ProfileForm(forms.ModelForm):
    nickname=forms.CharField(min_length=1,max_length=20,required=False,
                             error_messages={
                                 'min_length':'昵称至少4个字符',
                                 'max_length':'昵称不能多于20个字符'
                             },
                             widget=forms.TextInput())
    avatar=forms.ImageField(required=False,validators=[avatar_file_size],
                            widget=forms.FileInput(attrs={'class':'n'}))    #attrs自定义错误添加属性和样式
    email=forms.EmailField(required=False,error_messages={
                            'invalid':'请输入有效的Email地址',
                            },
                           widget=forms.EmailField())
    gender=forms.CharField(min_length=1,max_length=1,required=False,
                           widget=forms.HiddenInput())

    mobile=forms.CharField(min_length=11,max_length=11,required=False,
                           error_messages={
                               'min_length':'请输入11位手机号',
                               'max_length':'请输入11位手机号',
                           },
                           widget=forms.NumberInput())

    class Meta:
        model=User
        fields=['nickname','avatar','email','gender','mobile']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4,max_length=30,
                               error_messages={
                                   'min_length':'用户名不少于4个字符',
                                   'max_length':'用户名不能多于30个字符',
                                   'required':'用户名不能为空',

                               },
                               widget=forms.TextInput(attrs={'placeholder':'请输入用户名'}))

    password = forms.CharField(min_length=6,max_length=30,
                               error_messages={
                                   'min_length':'密码不少于6个字符',
                                   'max_length':'密码不能多于30个字符',
                                   'required':'密码不能为空'
                               },
                               widget=forms.TextInput(attrs={'placeholder'}))
    class Meta:
        model=User
        fields=['username','password']

    error_messages = {'invalid_login':'用户名名或密码错误',}


