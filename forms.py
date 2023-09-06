from django import forms
from .models import Coupon

class AddCouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = "__all__"