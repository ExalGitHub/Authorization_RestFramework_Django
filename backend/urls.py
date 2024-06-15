from django.contrib import admin
from django.urls import path, re_path

from .views import login, logout, profile, register, delete_user, update_user, staff

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login'   , login),
    re_path('logout'  , logout),
    re_path('register', register),
    re_path('profile' , profile),
    re_path('delete_user' , delete_user),
    re_path('update_user' , update_user),
    re_path('staff', staff),
]
