#自定义表单
import re



from django import forms
from django.core.exceptions import ValidationError


def check_password(password):
    if re.match(r'\d+$',password):
        raise ValidationError('密码不能是纯数字')

class UserForm(forms.Form):
    # username=forms.CharField(label='用户名:',max_length=20,min_length=3,
    #                          error_messages={
    #                         'required':'用户名必须输入','max_length':'用户名最大20字符','min_length':'用户名最小3字符'
    #                          })

    password_hash=forms.CharField(label='密码:',max_length=20,min_length=3,
                             widget=forms.PasswordInput(attrs={
                                 'placehold':'请输入密码',
                                 'class':'password'
                             }),
                             error_messages={
                                 'required': '密码必须输入', 'max_length': '密码最大20字符', 'min_length': '用户名最小3字符'
                             },
                             validators=[check_password]
                             )

    confirm_password=forms.CharField(label='确认密码',max_length=20,min_length=3,
                                     widget=forms.PasswordInput(attrs={
                                         'placehold': '请输入密码',
                                         'class': 'password'
                                     }),
                                     error_messages={
                                         'required': '密码必须输入', 'max_length': '密码最大20字符', 'min_length': '用户名最小3字符'
                                     },
                                     validators=[check_password]
                                     )


    # gender=forms.ChoiceField(label='性别:',choices=[(0,'女'),(1,'男'),(2,'保密')],
    #                          initial=1,
    #                          widget=forms.RadioSelect,
    #                          error_messages={
    #                              'required':'性别必须输入',
    #                              'invalid_choice':'无效选择'
    #                          }
    #                          )

    username=forms.CharField(label='手机号:',max_length=11,min_length=11,
                          error_messages={
                              'required':'手机号必须输入',
                              'max_length':'手机号长度11位',
                              'min_length':'手机号长度11位',
                          })


    #自定义验证字段
    #方法名规则：clean_字段名
    def clean_phono(self):
        #必须使用cleaned_data获取数据
        value=self.cleaned_data.get('phone')
        if re.match(r'1[3,5,6,7,8,9]\d{9}$',value):
            return value
        raise ValidationError('手机号码格式错误')

    #全局验证钩子函数
    def clean(self):
        password1=self.cleaned_data.get('password_hash')
        password2=self.cleaned_data.get('confirm_password')
        if password1==password2:
            return self.cleaned_data
        #错误信息可以是一个字典，字典的键应该是
        raise ValidationError({'confirm_password':'俩次密码不一致'})
