from django.db import models


class Supplier(models.Model):
    Name = models.CharField(max_length=250, blank=False)
    Country = models.CharField(max_length=250,blank=False)
    ContactNumber = models.CharField(max_length=11,blank=False)
    
    def __str__(self) -> str:
       return self.Name

   
class Category(models.Model):
    Name = models.CharField(max_length=250, blank=False)
    Details = models.CharField(max_length=250, blank=True)

    def __str__(self) -> str:
       return self.Name


class Product(models.Model):
  Name = models.CharField(max_length=250,blank=False)
  FeePrice = models.PositiveBigIntegerField(blank=False)
  CategoryId = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  SupplierId = models.ForeignKey(Supplier,on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return self.Name


class Employee(models.Model):
    FirstName = models.CharField(max_length=100,blank=False)   
    LastName = models.CharField(max_length=100,blank=False)   
    PhoneNumber = models.CharField(max_length=11,blank=False)

    def __str__(self) -> str:
       return self.FirstName + ' ' + self.LastName
   
   
class Customer(models.Model):
    FirstName = models.CharField(max_length=100,blank=False)   
    LastName = models.CharField(max_length=100,blank=False)   
    PhoneNumber = models.CharField(max_length=11,blank=False)

    def __str__(self) -> str:
       return self.FirstName + ' ' + self.LastName

class DeliverCo(models.Model):
    Name = models.CharField(max_length=100,blank=False)
    ContactNumber = models.CharField(max_length=11,blank=False)
    DeliverType = models.CharField(max_length=250,blank=False)
    
    def __str__(self) -> str:
       return self.Name


class Order(models.Model):
    CustomerId = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    EmployeeId = models.ForeignKey(Employee,  on_delete=models.DO_NOTHING)
    DeliveryTypeId = models.ForeignKey(DeliverCo, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
       return 'order' + self.Id



class OrderDetail(models.Model):
    ProductId = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    OrderId = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    Count = models.PositiveBigIntegerField(blank=False)
    FeePrice = models.PositiveBigIntegerField(blank=False)
    
    def __str__(self) -> str:
       return 'OrderDetail' + self.Id
   
   
   
   
   
   