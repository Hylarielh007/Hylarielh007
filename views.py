
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View

from mainapp.forms import AddCouponForm
from .models import *


class CouponView(View):
    def get(self, request):
        print("getting --------------> ")
        coupons = Coupon.objects.all()
        return render(request, 'mainapp/coupons.html', {'coupons': coupons})
    
def add_coupon_view(request):
    if request.POST:
        add_coupon = AddCouponForm(request.POST)
        if add_coupon.is_valid:
            add_coupon.save()
        else:
            raise Exception(add_coupon.errors)
        return redirect('coupons: coupons')
    
def delete_coupon_view(request, id):
    coupon = get_object_or_404(Coupon, pk=id)
    coupon.delete()
    return redirect('coupons: coupons')
    
    

class EmployeeView(View):
    def get(self, request):
        coupons = Coupon.objects.all()
        return render(request, 'mainapp/employee.html', {})
    
def add_employee_view(request):
    if request.POST:
        add_employee = AddCouponForm(request.POST)
        if add_employee.is_valid:
            add_employee.save()
        else:
            raise Exception(add_employee.errors)
        return redirect('coupons: coupons')
    
def delete_employee_view(request, id):
    employee = get_object_or_404(Coupon, pk=id)
    employee.delete()
    return redirect('coupons: coupons')

class VehicleView(View):
    def get(self, request):
        coupons = Coupon.objects.all()
        return render(request, 'mainapp/vehicle.html', {})
    
def add_vehicle_view(request):
    if request.POST: 
        add_vehicle = AddCouponForm(request.POST)
        if add_vehicle.is_valid:
            add_vehicle.save()
        else:
            raise Exception(add_vehicle.errors)
        return redirect('coupons: coupons')
    
def delete_vehicle_view(request, id):
        vehicle = get_object_or_404(Coupon, pk=id)
        vehicle.delete()
        return redirect('coupons: coupons')

def index(request):
    return render(request, 'index.html')


def add_Coupon(request):
    return render(request, 'index.html')
