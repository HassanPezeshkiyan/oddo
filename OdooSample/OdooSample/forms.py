from django import forms
from .models import *

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد نمایید', 'class': 'form-control valid'}),
        label="نام کاربری"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور خود را وارد نمایید', 'class': 'form-control valid'}),
        label="رمز عبور",
       
    )
class CreateProductForm(forms.ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام محصول را وارد کنید', 'class': 'form-control'}
    ))

    FeePrice = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'قیمت محصول را وارد کنید', 'class': 'form-control'}
    ))

    Category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        widget=forms.Select(
            attrs={'class': 'form-control'}
    ))

    Supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(), 
        widget=forms.Select(
            attrs={'class': 'form-control'}
    ))

    class Meta:
        model = Product
        fields = ['Name', 'FeePrice']


class CreateCategoryForm(forms.ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام دسته بندی را وارد کنید', 'class': 'form-control'}
    ))

    Details = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'توضیحات دسته بندی را وارد کنید', 'class': 'form-control'}
    ))

   
    class Meta:
        model = Category
        fields = ['Name', 'Details']
        
        
class CreateEmployeeForm(forms.ModelForm):
    FirstName = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام  را وارد کنید', 'class': 'form-control'}
    ))

    LastName = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'نام خانوادگی را وارد کنید', 'class': 'form-control'}
    ))
    PhoneNumber = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'شماره تلفن را وارد کنید', 'class': 'form-control'}
    ))
   
    class Meta:
        model = Employee
        fields = ['FirstName', 'LastName', 'PhoneNumber']        
       
        
class CreateCustomerForm(forms.ModelForm):
    FirstName = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام  را وارد کنید', 'class': 'form-control'}
    ))

    LastName = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'نام خانوادگی را وارد کنید', 'class': 'form-control'}
    ))
    PhoneNumber = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'شماره تلفن را وارد کنید', 'class': 'form-control'}
    ))
   
    class Meta:
        model = Customer
        fields = ['FirstName', 'LastName', 'PhoneNumber']        
        

class CreateSupplierForm(forms.ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام  را وارد کنید', 'class': 'form-control'}
    ))

    Countery = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'کشور را وارد کنید', 'class': 'form-control'}
    ))
    ContactNumber = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'شماره تماس را وارد کنید', 'class': 'form-control'}
    ))
   
    class Meta:
        model = Employee
        fields = ['Name', 'Countery', 'ContactNumber']
        
        
class CreateDeliverForm(forms.ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام  را وارد کنید', 'class': 'form-control'}
    ))

    ContactNumber = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'شماره تماس را وارد کنید', 'class': 'form-control'}
    ))
    DeliverType = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'نوع ارسال را وارد کنید', 'class': 'form-control'}
    ))
   
    class Meta:
        model = Deliver
        fields = ['Name', 'ContactNumber', 'DeliverType']