"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpRequest
from app.models import *
from django import forms
from app.forms import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def orders(request):
    """Renders the orders page."""
    assert isinstance(request, HttpRequest)
    orders = Orders.objects.all()
    return render(
        request,
        'app/orders.html',
        {
            'orders':orders,
            'title':'Orders',
            'year':datetime.now().year,
        }
    )

def invoices(request):
    """Renders the invoices page."""
    assert isinstance(request, HttpRequest)
    invoices = Invoice.objects.all()
    return render(
        request,
        'app/invoices.html',
        {
            'invoices':invoices,
            'title':'Invoices',
            'year':datetime.now().year,
        }
    )

def statements(request):
    """Renders the statements page."""
    assert isinstance(request, HttpRequest)
    statements = Statement.objects.all()
    return render(
        request,
        'app/statements.html',
        {
            'statements':statements,
            'title':'Statements',
            'year':datetime.now().year,
        }
    )

def customers(request):
    """Renders the customers page."""
    assert isinstance(request, HttpRequest)
    customers = Customer.objects.all()
    return render(
        request,
        'app/customers.html',
        {
            'customers':customers,
            'title':'Customers',
            'year':datetime.now().year,
        }
    )

def inventory(request):
    """Renders the inventory page."""
    assert isinstance(request, HttpRequest)
    inventory = Inventory.objects.all()
    return render(
        request,
        'app/inventory.html',
        {
            'inventory':inventory,
            'title':'Inventory',
            'year':datetime.now().year,
        }
    )

def vendors(request):
    """Renders the vendors page."""
    assert isinstance(request, HttpRequest)
    vendors = Vendor.objects.all()
    return render(
        request,
        'app/vendors.html',
        {
            'vendors':vendors,
            'title':'Vendors',
            'year':datetime.now().year,
        }
    )


def orderDetails(request, id):
    orders = Orders.objects.get(pk=id)
    return render_to_response('app/orderDetails.html', {'orders' : orders})


def addOrders(request):
    if request.method=="POST":
        form = orderForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else :
        form = orderForm()
        return render(request, 'app/addOrders.html', { 'form':form })


def invoiceDetails(request, id):
    invoices = Invoice.objects.get(pk=id)
    return render_to_response('app/invoiceDetails.html', {'invoices' : invoices})


def addInvoices(request):
    if request.method=="POST":
        form = invoiceForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else :
        form = invoiceForm()
        return render(request, 'app/addInvoice.html', { 'form':form })


def customerDetails(request, id):
    customers = Customer.objects.get(pk=id)
    return render_to_response('app/customerDetails.html', {'customers' : customers})


def addCustomers(request):
    if request.method=="POST":
        form = customerForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else :
        form = customerForm()
        return render(request, 'app/addCustomers.html', { 'form':form })


def vendorDetails(request, id):
    vendors = Vendor.objects.get(pk=id)
    return render_to_response('app/vendorDetails.html', {'vendors' : vendors})


def addVendors(request):
    if request.method=="POST":
        form = vendorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else :
        form = vendorForm()
        return render(request, 'app/addVendors.html', { 'form':form })


def inventoryDetails(request, id):
    inventory = Inventory.objects.get(pk=id)
    return render_to_response('app/inventoryDetails.html', {'inventory' : inventory})


def addInventory(request):
    if request.method=="POST":
        form = inventoryForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else :
        form = inventoryForm()
        return render(request, 'app/addInventory.html', { 'form':form })

def statementDetails(request, id):
    statements = Statement.objects.get(pk=id)
    return render_to_response('app/statementDetails.html', {'statements' : statements})


def addStatements(request):
    if request.method=="POST":
        form = statementForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')

    else :
        form = statementForm()
        return render(request, 'app/addStatements.html', { 'form':form })