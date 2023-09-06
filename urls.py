
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'coupons'

urlpatterns = [
    path('',index,name='index'),
    path('coupons', CouponView.as_view(), name='coupons'), 
    path('coupons/add', add_coupon_view, name='add'), 
    path('coupons/delete/<str:id>', delete_coupon_view, name='delete'), 
    
    path('employees', EmployeeView.as_view(), name='employees'),
    path('employee/add', add_employee_view, name='add'),
    path('employee/delete/<str:id>', delete_employee_view, name='delete'),
    
    path('vehicles', VehicleView.as_view(), name='vehicles'),
    path('vehicle/add', add_vehicle_view, name='add'),
    path('vehicle/delete/<str:id>', delete_vehicle_view, name='delete'),
    #path('add_Coupons',index, name='add_Coupons')#
]