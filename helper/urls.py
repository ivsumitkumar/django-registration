from django.urls import path
from . import views

urlpatterns = [
    path('',views.sighUpPage, name='signup'),
    path('signup/',views.sighUpPage, name='signup'),
    path('login/',views.logInPage, name='login'),
    path('home/',views.homePage, name='home'),
    path('logout/',views.LogOutPage,name='logout'),
]
