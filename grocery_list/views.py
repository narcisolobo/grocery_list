from django.shortcuts import render, redirect
from .models import User, Store, Product

def index(request):
    context = {
        'users': User.objects.all(),
        'stores': Store.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)

def users_new(request):
    user = User.objects.create(name = request.POST['name'])
    request.session['user_id'] = user.id
    return redirect('/')

def stores_new(request):
    creator = User.objects.get(id = request.session['user_id'])
    store = Store.objects.create(
        name = request.POST['name'],
        creator = creator
    )
    return redirect('/')

def products_new(request):
    creator = User.objects.get(id = request.session['user_id'])
    product = Product.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        quantity = request.POST['quantity'],
        price = request.POST['price'],
        creator = creator
    )
    return redirect('/')