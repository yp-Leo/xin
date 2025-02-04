# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-12 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('addressname', models.CharField(max_length=200)),
                ('recipientsname', models.CharField(max_length=60)),
                ('recipientstel', models.IntegerField(max_length=11)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=60, unique=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('goodname', models.CharField(max_length=60, unique=True)),
                ('ispost', models.IntegerField(default=0)),
                ('likenum', models.IntegerField(default=0)),
                ('addtime', models.DateTimeField(auto_now=True)),
                ('coverphoto', models.CharField(max_length=600, null=True)),
                ('category', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='App.Category')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Pastry',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1000)),
                ('photo', models.CharField(max_length=600, null=True)),
                ('cart', models.IntegerField(default=0)),
                ('goods', models.OneToOneField(db_column='gid', on_delete=django.db.models.deletion.CASCADE, related_name='pastry', to='App.Goods')),
            ],
            options={
                'db_table': 'pastry',
            },
        ),
        migrations.CreateModel(
            name='Shopcart',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.IntegerField(default=1)),
                ('totalprice', models.IntegerField(default=0)),
                ('address', models.ForeignKey(db_column='aid', on_delete=django.db.models.deletion.CASCADE, related_name='shopcart', to='App.Address')),
                ('pastry', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.CASCADE, related_name='shopcart', to='App.Pastry')),
            ],
            options={
                'db_table': 'shopcart',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=60, null=True, unique=True)),
                ('password_hash', models.CharField(db_column='password', max_length=128)),
                ('sex', models.IntegerField(blank=True, null=True, verbose_name='性别')),
                ('realname', models.CharField(max_length=60, null=True)),
                ('tel', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('birthday', models.DateTimeField(null=True)),
                ('qq', models.IntegerField(null=True)),
                ('grade', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'wdm_user',
                'ordering': ['username'],
            },
        ),
        migrations.AddField(
            model_name='shopcart',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, related_name='shopcart', to='App.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(db_column='uid', on_delete=django.db.models.deletion.CASCADE, related_name='address', to='App.User'),
        ),
    ]
