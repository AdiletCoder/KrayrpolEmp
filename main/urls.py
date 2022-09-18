"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from employer.views import CompanyListView, CompanyDetailView, EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, SearchListView, CompanyCreateView, CompanyUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CompanyListView.as_view(), name='home'),
    path('company/<str:slug>/', CompanyDetailView.as_view(), name='company-detail'),
    path('/create/', CompanyCreateView.as_view(), name='create-company'),
    path('company/update/<str:slug>/', CompanyUpdateView.as_view(), name='update-company'),
    path('<str:slug>/', EmployeeListView.as_view(), name='emp-list'),
    path('employee/<int:employee_id>/', EmployeeDetailView.as_view(), name='detail'),
    path('employee/create/', EmployeeCreateView.as_view(), name='create-employee'),
    path('employee/update/<int:employee_id>/', EmployeeUpdateView.as_view(), name='update-employee'),
    path('employee/delete/<int:employee_id>/', EmployeeDeleteView.as_view(), name='delete-employee'),
    path('search', SearchListView.as_view(), name='search'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
