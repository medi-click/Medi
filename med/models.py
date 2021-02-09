from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.urls import reverse



class IProduct(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    medicine_name=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.medicine_name


        
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=225)
    # slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[self.pk])
    # @property
    # def get_product(self):
    #     return Product.objects.filter(categories__title=self.title)


class Product(models.Model):
    # CATEGORY = (
    #     ('Healthcare', 'Healthcare'),
    #     ('Medicine', 'Medicine'),
    #     ('COVID-19','COVID-19'),

    # )
    name = models.CharField(max_length=200, null=True)
    manufacturered_by = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    image = models.ImageField(null=True,blank=True)
    categories = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank= True)
    date_created =  models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def set_absolute_url(self):
       return reverse('product_details',args=[self.pk,])


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered'),
        )

    #customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    
class OrderItem(models.Model):
    product= models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class WishItem(models.Model):
    product= models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity_wish = models.IntegerField(default=0,null=True,blank=True)


class ShippingAddress(models.Model):
	# customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	# order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True,unique=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    postcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name