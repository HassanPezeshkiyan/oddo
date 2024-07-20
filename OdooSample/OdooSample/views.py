from django.shortcuts import render,redirect
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.views.generic import *
from .models import *
from .forms import *
from django.db.models import Sum
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    context = {
        "login_form": login_form
    }
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            context["login_form"] = LoginForm()
            return redirect('/login')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')
    return render(request, 'login.html', context)

def Index(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    delivers = Deliver.objects.all()
    customers = Customer.objects.all()
    employees = Employee.objects.all()
    suppliers = Supplier.objects.all()
    orders = Order.objects.all()
    orderDetails = OrderDetail.objects.all()
    productSum = products.aggregate(Sum('FeePrice'))['FeePrice__sum']
    orderAvg = orderDetails.count() / orders.count()
    # ordersSum = orderDetails.annotate(
    # result=F('FeePrice') * F('Count')).first()
    
    return render(request,'index.html',context={
        'productCount':products.count(),
        'products':products,
        'categoryCount':categories.count(),
        'categories':categories,
        'employeeCount' : employees.count(),
        'emoloyees': employees,
        'customerCount' : customers.count(),
        'customers': customers,
        'deliverCount' : delivers.count(),
        'delivers': delivers,
        'suppliers':suppliers,
        'supplierCount':suppliers.count(),
        'orderCount':orders.count(),
        'orders':orders,
        'productSum':productSum,
        'orderAvg':orderAvg
    })
    
def search(request):        
    if request.method == 'GET': # this will be GET now      
        q =  request.GET.get('search') # do some research what it does       
        product = Product.objects.filter(Name__contains = q) # filter returns a list so you might consider skip except part
        return render(request,"search.html",{"search":product})
        
    else:
        return render(request,"search.html",{})    

class ProductListView(ListView):
    model = Product
    
class CategoryListView(ListView):
    model = Category
    
class OrderListView(ListView):
    model = Order
    
class OrderDetailListView(ListView):
    model = OrderDetail
    
class EmployeeListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    model = Employee
    
    
    
    
class CustomerListView(ListView):
    model = Customer
    
class DeliverListView(ListView):
    model = Deliver
    
class SupplierListView(ListView):
    model = Supplier
    

class CreateProduct(CreateView):
    model = Product
    template_name = 'product/add_Product.html'
    form_class = CreateProductForm
    success_url = '/proudcts'
  
class CreateCategory(CreateView):
    model = Category
    template_name = 'category/add_Category.html'
    form_class = CreateCategoryForm
    success_url = '/categories'

class CreateSupplier(CreateView):
    model = Supplier
    template_name = 'supplier/add_Supplier.html'
    form_class = CreateSupplierForm
    success_url = '/suppliers'
    
class CreateDeliver(CreateView):
    model = Deliver
    template_name = 'deliver/add_Deliver.html'
    form_class = CreateDeliverForm
    success_url = '/delivers'

class CreateCustomer(CreateView):
    model = Customer
    template_name = 'customer/add_Customer.html'
    form_class = CreateCustomerForm
    success_url = '/customers'
    
class CreateEmployee(CreateView):
    model = Employee
    template_name = 'employee/add_Employee.html'
    form_class = CreateEmployeeForm
    success_url = '/empolyees'


class CategoryUpdate(UpdateView):
    model = Category
    fields = ["Name","Details"]
    template_name = "category/update_Category.html"
    success_url = '/categories'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ["FirstName","LastName",'PhoneNumber']
    template_name = "employee/update_Employee.html"
    success_url = '/employees'

class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CreateCustomerForm
    # fields = ["FirstName","LastName",'PhoneNumber']
    template_name = "customer/update_Customer.html"
    success_url = '/customers'

class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ["Name","Details"]
    template_name = "supplier/update_Supplier.html"
    success_url = '/suppliers'
    
class DeliverUpdate(UpdateView):
    model = Deliver
    fields = ["Name","Details"]
    template_name = "deliver/update_Deliver.html"
    success_url = '/delivers'

class ProductUpdate(UpdateView):
    model = Product
    fields = ["Name","Details"]
    template_name = "product/update_Product.html"
    success_url = '/products'

class OrderDetailUpdate(UpdateView):
    model = OrderDetail
    fields = []
    template_name = ""
    success_url = ""


class CategoryDelete(DeleteView):
    model = Category
    template_name = "category/delete_Category.html"
    success_url = '/categories'
    
class ProductDelete(DeleteView):
    model = Product
    template_name = "product/delete_Product.html"
    success_url = '/proudcts'
    
class CustomerDelete(DeleteView):
    model = Customer
    template_name = "customer/delete_Customer.html"
    success_url = '/customer'

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = "employee/delete_Employee.html"
    success_url = '/employees'

class SupplierDelete(DeleteView):
    model = Supplier
    template_name = "supplier/delete_Supplier.html"
    success_url = '/suppliers'
    
class DeliverDelete(DeleteView):
    model = Deliver
    template_name = "deliver/delete_Deliver.html"
    success_url = '/delivers'
    
class OrderDelete(DeleteView):
    model = Order
    template_name = "order/delete_Order.html"
    success_url = '/orders'
    
class OrderDetailDelete(DeleteView):
    model = OrderDetail
    template_name = "orderDetail/delete_OrderDetail.html"
    success_url = '/orderDetails'
    

class ProductDetail(DetailView):
    model = Product

class CategoryDetail(DetailView):
    model = Category

class SupplierDetail(DetailView):
    model = Supplier

class DeliverDetail(DetailView):
    model = Deliver

class EmployeeDetail(DetailView):
    model = Employee

class CustomerDetail(DetailView):
    model = Customer




    