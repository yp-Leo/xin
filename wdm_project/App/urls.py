from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^base/$',views.base,name='base'),
    url(r'^index/$',views.index,name='index'),
    url(r'^nav_br1/$',views.nav_br1,name='nav_br1'),
    url(r'^nav_br2/$',views.nav_br2,name='nav_br2'),
    url(r'^nav_br3/$',views.nav_br3,name='nav_br3'),
    url(r'^nav_br4/$',views.nav_br4,name='nav_br4'),
    url(r'^nav_br5/$',views.nav_br5,name='nav_br5'),
    url(r'^nav_br6/$',views.nav_br6,name='nav_br6'),
    url(r'^nav_br7/$',views.nav_br7,name='nav_br7'),

]