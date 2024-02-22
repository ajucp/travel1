from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name="demo"),
    # path('registration/', views.credential, name="credential")
    path('add/',views.addition,name="addition")

]