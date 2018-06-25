from  django.conf.urls import  url
from  booktest import views

urlpatterns = [
    url(r'^(?P<pIndex>[0-9]*)$',views.index,name='index'),
    url(r'^detail$', views.detail,name='detail'),
    url(r'^create$', views.create,name='create'),
    url(r'^delete(\d+)$',views.delete,name='delete'),
    url(r'^json1$', views.json1,name='json1'),
    url(r'^my_ajax$', views.my_ajax,name='my_ajax'),
    url(r'^my_static$', views.my_static, name='my_static'),

]