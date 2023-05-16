"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from pdf import views

app_name = 'pdf'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name='accept'),
    path('<int:pk>/', views.resume, name='resume'),
    path('list/', views.list, name='list'),
    path('convert/', views.convert_to_pdf, name='convert_to_pdf'),
    path('bedjo/', views.see, name='see'),
    path('bedjo2/', views.bedjo2, name='see'),
    path('bedjo3/', views.bedjo3, name='see'),
    path('bedjo4/', views.bedjo4, name='see'),
    path('bedjo5/', views.bedjo5, name='see'),
]
