"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Customer(models.Model):
    company_name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    billing_address = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    email = models.EmailField( max_length = 254)

    def __str__(self):
        return self.company_name

class Inventory(models.Model):
    item_name = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    expiration = models.DateField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.item_name

class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchaser_name = models.CharField(max_length = 30)
    shipping_address = models.CharField(max_length = 30)
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivery_date = models.DateField()

    def __str__(self):
        return self.purchaser_name

class Invoice(models.Model):
    orders_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item_name = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    due_date = models.DateField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    paid_status =  models.BooleanField()

    def __str__(self):
        return self.item_name

class Vendor(models.Model):
    company_name = models.CharField(max_length = 30)
    payment_address = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    email = models.EmailField( max_length = 254)

    def __str__(self):
        return self.company_name

class Statement(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 30)
    billing_address = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    due_date = models.DateField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    paid_status =  models.BooleanField()

    def __str__(self):
        return self.item_name