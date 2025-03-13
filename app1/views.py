from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product,Category,Contact


# Create your views here.
def index(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'index.html', {'products': products})  # Pass products to the template

def about(request):
    return render(request, 'about.html')  # Render 'about.html'

def menu(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'menu.html', {'products': products})  # Pass products to the template

def blog(request):
    return render(request, 'blog.html')  # Render 'blog.html'

def contact(request):
    return render(request, 'contact.html')  # Render 'contact.html'

def order(request):
    cat = Category.objects.all()
    products = {category: Product.objects.filter(category=category) for category in cat}
    return render(request, 'order.html', {'products': products, 'category': cat,})

def productDetail(request, name):
    product_info = get_object_or_404(Product, name=name)
    related_products = Product.objects.filter(category=product_info.category).exclude(id=product_info.id)[:4]  # Limit to 4 related products
    context = {"productInfo": product_info,
                "related_products": related_products
               }  # Pass the product info to the template
    return render(request, 'product.html', context)

def productCategory(request, category_name):
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'order.html', {'category': category, 'products': products})

def save_contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        if first_name and last_name and email and phone_number and message:
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Please fill in all fields.'})