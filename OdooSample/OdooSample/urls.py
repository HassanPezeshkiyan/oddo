"""
URL configuration for OdooSample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('', Index,name='index'),
    path("admin/", admin.site.urls),
    
    path("order/", OrderListView.as_view(),name ='order-list'),
    path("orderDetails/", OrderDetailListView.as_view(),name ='orderDetail-list'),
    
    path("products/", ProductListView.as_view(),name ='proudct-list'),
    path("product/create", CreateProduct.as_view(), name = 'product-create'),
    path("product/update/<int:pk>", ProductUpdate.as_view(), name = 'product-update'),
    path("product/delete/<int:pk>", ProductDelete.as_view(), name = 'product-delete'),
    path("product/<int:pk>", ProductDetail.as_view(), name = 'product-detail'),
    
    path("categories/", CategoryListView.as_view(), name ='category-list'),
    path("category/create", CreateCategory.as_view(), name = 'category-create'),
    path("category/update/<int:pk>", CategoryUpdate.as_view(), name = 'category-update'),
    path("category/delete/<int:pk>", CategoryDelete.as_view(), name = 'category-delete'),
    path("category/<int:pk>", CategoryDetail.as_view(), name = 'category-detail'),
    
    path("employees/", EmployeeListView.as_view(),name ='employee-list'),
    path("employee/create", CreateEmployee.as_view(), name = 'employee-create'),
    path("employee/update/<int:pk>", EmployeeUpdate.as_view(), name = 'employee-update'),
    path("employee/delete/<int:pk>", EmployeeDelete.as_view(), name = 'employee-delete'),
    path("employee/<int:pk>", EmployeeDetail.as_view(), name = 'employee-detail'),
    
    path("customers/", CustomerListView.as_view(),name ='customer-list'),
    path("customer/create", CreateCustomer.as_view(), name = 'customer-create'),
    path("customer/update/<int:pk>", CustomerUpdate.as_view(), name = 'customer-update'),
    path("customer/delete/<int:pk>", CustomerDelete.as_view(), name = 'customer-delete'),
    path("customer/<int:pk>", CustomerDetail.as_view(), name = 'customer-detail'),
    
    path("suppliers/", SupplierListView.as_view(),name ='supplier-list'),
    path("supplier/create", CreateSupplier.as_view(), name = 'supplier-create'),
    path("supplier/update/<int:pk>", SupplierUpdate.as_view(), name = 'supplier-update'),
    path("supplier/delete/<int:pk>", SupplierDelete.as_view(), name = 'supplier-delete'),
    path("supplier/<int:pk>", SupplierDetail.as_view(), name = 'supplier-detail'),
    
    path("delivers/", DeliverCoListView.as_view(),name ='deliver-list'),
    path("deliver/create", CreateDeliverCo.as_view(), name = 'deliver-create'),
    path("deliver/update/<int:pk>", DeliverUpdate.as_view(), name = 'deliver-update'),
    path("deliver/delete/<int:pk>", DeliverDelete.as_view(), name = 'deliver-delete'),
    path("deliver/<int:pk>", DeliverDetail.as_view(), name = 'deliver-detail'),
]
