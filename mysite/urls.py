"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('regist/', views.register),
    path('logout/', views.logout),
    path('release_task/', views.release_task),
    path('all_task/', views.all_task),
    path('enter_task/', views.enter_task),
    path('check_task/', views.check_task),
    path('one_task/', views.one_task),
    path('recharge/', views.recharge),

    # path('task/get_all_tasks/', views.get_all_tasks, name='get_all_tasks'),
    # path('task/get_user_tasks/', views.get_user_tasks, name='get_user_tasks'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
