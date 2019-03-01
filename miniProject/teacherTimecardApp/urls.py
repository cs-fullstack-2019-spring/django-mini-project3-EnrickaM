from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('all/', views.all, name="index"),
    path("create/",views.create,name='index'),
    path('update/',views.updat,name='index'),

]