from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *


def Index(request):
    productCount = Product.objects.count()
    categories = Category.objects.all()
    print(categories)
    return render(request,'index.html',context={
        'productCount':productCount,
        'categories':categories
    })





class ProductListView(ListView):
    model = Product
    
class CategoryListView(ListView):
    model = Category
    
class OrderListView(ListView):
    model = Order
    
class OrderDetailListView(ListView):
    model = OrderDetail
    
class EmployeeListView(ListView):
    model = Employee
    
class CustomerListView(ListView):
    model = Customer
    
class DeliverCoListView(ListView):
    model = DeliverCo
    
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
    
class CreateDeliverCo(CreateView):
    model = DeliverCo
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
    fields = ["Name","Details"]
    template_name = "employee/update_Employee.html"
    success_url = '/employees'

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ["Name","Details"]
    template_name = "customer/update_Customer.html"
    success_url = '/customers'

class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ["Name","Details"]
    template_name = "supplier/update_Supplier.html"
    success_url = '/suppliers'
    
class DeliverUpdate(UpdateView):
    model = DeliverCo
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
    model = DeliverCo
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
    model = DeliverCo

class EmployeeDetail(DetailView):
    model = Employee

class CustomerDetail(DetailView):
    model = Customer




    