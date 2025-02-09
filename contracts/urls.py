
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
    path('', views.home_sidebar , name='home_sidebar'),
    path('create_contract/', views.create_contract, name='create_contract'),
    path('contract_list/', views.contract_list, name="contractlist"),  # بدون پارامتر  
    path('delete_contract/<int:contract_id>/', views.delete_contract, name='delete_contract'),
    path('edit_contract/<int:contract_id>/', views.edit_contract, name='edit_contract'),
    path('pdf/<int:contract_id>/', views.generate_pdf, name='generate_pdf'),
    #path('/about', views.contract_list),   اگر در اینجا روی تب ثبت قرارداد جدید اومد یا کلیک کرد یه لیست کشویی باز بشه
    #path('/about', views.about),   اگر در اینجا روی تب مشاهد و جستجو اومد یا کلیک کرد یه لیست کشویی باز بشه  
    path('contract_list/personnel/', views.personnel_view, name='personel'),
    path('contract_list/outstanding/', views.outstanding_view, name='outstanding'),
    path('contract_list/nda/', views.nda_view, name='nda'),
    path('contract_list/partnership/', views.partnership_view, name='partnership'),
]
