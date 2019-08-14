import hashlib

from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)                                         # 用户id
    username = models.CharField(unique=True, max_length=60, blank=True, null=True)   # 用户名
    password_hash = models.CharField(max_length=128, db_column='password')           # 用户密码
    sex = models.IntegerField(blank=True, null=True, verbose_name='性别')             # 用户性别
    realname = models.CharField(max_length=60, null=True)                            # 用户真实姓名
    tel = models.IntegerField(max_length=11)                                         # 手机号
    email = models.EmailField(null=True)                                             # 邮箱
    birthday = models.DateTimeField(null=True)                                       # 生日
    qq = models.IntegerField(null=True)                                              # qq号
    integral = models.IntegerField(default=0)                                        # 积分

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        # self.password_hash = hashlib.sha1(value.encode('utf8')).hexdigest()
        self.password_hash = make_password(value)

    def check_pw(self,value):
        #第一参数是未加密的原文
        #第二个参数是加密后的秘文
        return check_password(value,self.password_hash)

    @classmethod
    def check_login1(cls,username,password):
        #按用户名查询
        user = cls.objects.filter(username=username).first()
        # 判定用户名是否正确，正确返回对象，否则None
        # if not user:
        #     return False
        # # 验证密码是否正确
        # if not check_password(password,user.password_hash):
        #     return False
        # return True
        # return user and check_password(password,user.password_hash)
        return user

    @classmethod
    def check_login2(cls, username, password):
        # 按用户名查询
        user = cls.objects.filter(email=username).first()
        # 判定用户名是否正确，正确返回对象，否则None
        # if not user:
        #     return False
        # # 验证密码是否正确
        # if not check_password(password,user.password_hash):
        #     return False
        # return True
        return user and check_password(password, user.password_hash)

    @property
    def gender(self):
        if self.sex == 1:
            return "女"
        return "男"

    class Meta:
        db_table = 'wdm_user'
        # abstract = True
        # managed = False
        ordering = ['username']


class Category(models.Model):
    cid = models.AutoField(primary_key=True)                                        # 板块id
    categoryname = models.CharField(max_length=60, unique=True)                     # 板块名
    pid = models.IntegerField(null=True, blank=True)                                # 板块对应糕点

    class Meta:
        db_table = 'category'


class Goods(models.Model):                                                          #
    gid = models.AutoField(primary_key=True)                                        # 商品id(蛋糕、月饼)
    goodname = models.CharField(max_length=60, unique=True)                         # 商品名字
    ispost = models.IntegerField(default=0)                                         # 是否展示（不同限定条件）
    likenum = models.IntegerField(default=0)                                        # 喜欢量
    addtime = models.DateTimeField(auto_now=True)                                   # 添加时间
    coverphoto = models.CharField(max_length=600, null=True)                        # 首页展示图片
    category = models.ForeignKey(to=Category,                                       # 一对多外键
                                 on_delete=models.CASCADE,                          # 级联删除
                                 db_column='cid',                                   # 表中字段名
                                 related_name='goods'                               # 通过用户查询detail的时候的引用
                                 )

    class Meta:
        db_table = 'goods'


# 糕点表
class Pastry(models.Model):
    pid = models.AutoField(primary_key=True)                                        # 
    size = models.CharField(max_length=100)
    price = models.IntegerField(default=1000)
    photo = models.CharField(max_length=600, null=True)
    cart = models.IntegerField(default=0)
    goods = models.OneToOneField(to=Goods,
                                 on_delete=models.CASCADE,  # 级联删除
                                 db_column='gid',  # 表中字段名
                                 related_name='pastry'  # 通过用户查询detail的时候的引用
                                 )

    class Meta:
        db_table = 'pastry'


# 收货地址
class Address(models.Model):
    aid = models.AutoField(primary_key=True)
    addressname = models.CharField(max_length=200)
    recipientsname = models.CharField(max_length=60)
    recipientstel = models.IntegerField(max_length=11)
    user = models.OneToOneField(to=User,
                                on_delete=models.CASCADE,  # 级联删除
                                db_column='uid',  # 表中字段名
                                related_name='address'  # 通过用户查询detail的时候的引用
                                )

    class Meta:
        db_table = 'address'


# 用户购物车
class Shopcart(models.Model):
    sid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,  # 级联删除
                             db_column='uid',  # 表中字段名
                             related_name='shopcart'  # 通过用户查询detail的时候的引用
                             )

    pastry = models.ForeignKey(to=Pastry,
                               on_delete=models.CASCADE,  # 级联删除
                               db_column='pid',  # 表中字段名
                               related_name='shopcart'  # 通过用户查询detail的时候的引用
                               )
    address = models.ForeignKey(to=Address,
                                on_delete=models.CASCADE,  # 级联删除
                                db_column='aid',  # 表中字段名
                                related_name='shopcart'  # 通过用户查询detail的时候的引用
                                )
    num = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=0)

    class Meta:
        db_table = 'shopcart'
