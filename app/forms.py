"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class customerForm(forms.ModelForm):
    class Meta :
        model = Customer
        labels = {
            "company_name" : "Company Name",
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "billing_address" : "Billing Address",
            "phone" : "Phone Number",
            "email" : "Email"
           }
        fields = ['company_name', 'first_name', 'last_name', 'billing_address', 'phone', 'email']

class orderForm(forms.ModelForm):
    class Meta :
        model = Orders
        labels = {
            "customer_id" : "Company Name",
            "purchaser_name" : "Purchaser Name (Include Company)",
            "shipping_address" : "Shipping Address",
            "inventory_id" : "Item Name",
            "quantity" : "Quantity",
            "delivery_date" : "Delivery Date (YYYY-MM-DD)"
           }
        fields = ['customer_id', 'purchaser_name', 'shipping_address', 'inventory_id', 'quantity', 'delivery_date']

class invoiceForm(forms.ModelForm):
    class Meta :
        model = Invoice
        labels = {
            "orders_id" : "Order ID",
            "item_name" : "Item Name (Include Company)",
            "quantity" : "Quantity",
            "due_date" : "Due Date (YYYY-MM-DD)",
            "total_price" : "Total Price (0.00)",
            "paid_status" : "Paid Status"
           }
        fields = ['orders_id', 'item_name', 'quantity', 'due_date', 'total_price', 'paid_status']

class vendorForm(forms.ModelForm):
    class Meta :
        model = Vendor
        labels = {
            "company_name" : "Company Name",
            "payment_address" : "Payment Address",
            "phone" : "Phone Number",
            "email" : "Email"
           }
        fields = ['company_name', 'payment_address', 'phone', 'email']

class inventoryForm(forms.ModelForm):
    class Meta :
        model = Inventory
        labels = {
            "item_name" : "Item Name",
            "quantity" : "Quantity",
            "expiration" : "Expiration (YYYY-MM-DD)",
            "item_price" : "Item Price"
           }
        fields = ['item_name', 'quantity', 'expiration', 'item_price']

class statementForm(forms.ModelForm):
    class Meta :
        model = Statement
        labels = {
            "invoice_id" : "Invoice ID",
            "company_name" : "Company",
            "billing_address" : "Billing Address",
            "phone" : "Phone Number",
            "due_date" : "Due Date (YYYY-MM-DD)",
            "total_price" : "Total Price",
            "paid_status" : "Paid Status"
           }
        fields = ['invoice_id', 'company_name', 'billing_address', 'phone', 'due_date', 'total_price', 'paid_status']