from django.conf.urls import url

from users import views

urlpatterns=[
    url(r'^$',views.users),
    url(r'^login/$',views.login),
    url(r'^signup/$',views.signup),
    url(r'^logout/$',views.logout),






]