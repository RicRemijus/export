from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Subscriber
from .forms import ProductForm, SubscriptionForm


# Create your views here.

#Helper Function: Only aalow superusers
def is_owner(user):
    return user.is_superuser

def product_list(request):
    products = Product.objects.all()
    for product in products:
        if not product.slug:
            product.slug = slugify(product.name)
            product.save()
    return render(request, "index.html", {'products':products})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    return render(request, 'product_detail.html', {'product':product, 'images':images})

@login_required
@user_passes_test(is_owner) 
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    
    return render(request, 'product_form.html', {'form': form})


@login_required
@user_passes_test(is_owner)
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ProductForm(instance=product)
        return render(request, 'product_form.html', {'form':form})
    
@login_required
@user_passes_test(is_owner)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    return render(request, 'index.html', {'product':product})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            return redirect('/')
        else:
            messages.error(request, "Subscription failed, please enter a valid email.")
    else:
        form = SubscriptionForm()
    return render(request, 'index.html', {'form':form})

def unsubscribe(request, email):
    try:
        subscriber = Subscriber.objects.get(email=email)
        subscriber.is_active = False
        subscriber.save()
        messages.success(request, "You have successfully unsubscribed!")
    except Subscriber.DoesNotExist:
        messages.error(request, "Email not found.")
    return redirect("/")