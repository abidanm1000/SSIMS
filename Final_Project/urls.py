"""
Definition of urls for Final_Project.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
admin.autodiscover()


urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.orders, name='orders'),
    path('invoices/', views.invoices, name='invoices'),
    path('statements/', views.statements, name='statements'),
    path('customers/', views.customers, name='customers'),
    path('inventory/', views.inventory, name='inventory'),
    path('vendors/', views.vendors, name='vendors'),
    path('addOrders/', views.addOrders, name='addOrders'),
    path('orders/<id>/', views.orderDetails, name='orderDetails'),
    path('addInvoices/', views.addInvoices, name='addInvoices'),
    path('invoices/<id>/', views.invoiceDetails, name='invoiceDetails'),
    path('addCustomers/', views.addCustomers, name='addCustomers'),
    path('customers/<id>/', views.customerDetails, name='customerDetails'),
    path('addVendors/', views.addVendors, name='addVendors'),
    path('vendors/<id>/', views.vendorDetails, name='vendorDetails'),
    path('addInventory/', views.addInventory, name='addInventory'),
    path('inventory/<id>/', views.inventoryDetails, name='inventoryDetails'),
    path('addStatements/', views.addStatements, name='addStatements'),
    path('statements/<id>/', views.statementDetails, name='statementDetails'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
