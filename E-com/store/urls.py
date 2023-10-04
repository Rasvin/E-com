
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginn,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('Device/<str:name>',views.Mobile,name="Mobile"),
    path('det/<str:cate_name>/<str:prod_name>',views.det,name="det")
 
]
