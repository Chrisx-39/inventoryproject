from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products,Order,Plant
from .forms import ProductsForm , OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
   orders = Order.objects.all()
   products = Products.objects.all()
   workers_count= User.objects.all().count()
   products_count= Products.objects.all().count()
   orders_count= Order.objects.all().count()
   if request.method =='POST':
       form = OrderForm(request.POST)
       if form.is_valid():
           instance = form.save(commit=False)
           instance.staff = request.user
           instance.save()
           return redirect ('dashboard-index')
   else:
       form = OrderForm()
   context = {
       'orders':orders,
       'form':form,
       'products':products,
       'workers_count':workers_count,
       'products_count':products_count,
       'orders_count':orders_count
   }
   return render(request,'dashboard/index.html',context)
@login_required
def staff(request):
    workers= User.objects.all()
    workers_count = workers.count() 
    products_count= Products.objects.all().count()
    orders_count= Order.objects.all().count()
    context= {
        'workers':workers,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count

    }
    return render(request,'dashboard/staff.html',context)
@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render (request,'dashboard/staff_detail.html',context)

@login_required
def product(request):
    items = Products.objects.all()
    ##items = Products.objects.raw('SELECT * FROM dashboard_products')
    workers_count= User.objects.all().count()
    products_count= Products.objects.all().count()
    orders_count= Order.objects.all().count()
    if request.method =='POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name}has been added')
            return redirect('dashboard-product')
    else:
        form = ProductsForm()
    context={
        'items' : items,
        'form':form,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count

    }
    return render(request,'dashboard/product.html',context)
@login_required
def product_delete(request,pk):
    item = Products.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

@login_required
def order_approve(request,pk):
    orders = Order.objects.get(id=pk)
    if request.method=='POST':
        orders.delete()
        return redirect('dashboard-order')
    return render(request,'dashboard/order_approval.html')

@login_required
def product_update(request,pk):
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductsForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductsForm(instance=item)
        
    context={
        'form':form,

    }
    return render(request,'dashboard/product_update.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    workers_count= User.objects.all().count()
    products_count= Products.objects.all().count()
    orders_count= Order.objects.all().count()
    context = {
        'orders': orders,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count
    }
    return render(request,'dashboard/order.html',context)


def plant(request):

    items = Plant.objects.all()
    items_count = Plant.objects.all().count()

    context = {
        'items': items,
        'items_count':items_count
    }

    return render(request,'dashboard/plant.html',context)
