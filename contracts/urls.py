"""
URL configuration for jango_contracts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path 
from . import views


app_name = 'contracts'

urlpatterns = [
    path('', views.side_barlist, name='sidebarlist'),
    path('create/', views.create_contract, name='create_contract'),
    #path('/about', views.contract_list),   اگر در اینجا روی تب ثبت قرارداد جدید اومد یا کلیک کرد یه لیست کشویی باز بشه
    #path('/about', views.about),   اگر در اینجا روی تب مشاهد و جستجو اومد یا کلیک کرد یه لیست کشویی باز بشه  
]
