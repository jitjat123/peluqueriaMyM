from django.urls import path
from peluqueriamimapp import views

urlpatterns = [

    path('',views.home,name="Inicio"),
    

]