import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from bboard.models import Phone

def show_catalog(request):
    catalog = Phone.objects.all()
    template = 'catalog.html'
    context = {"catalog": catalog}
    return render(request, template, context)

def time(request):
    return HttpResponse(f'Time {datetime.time}')

def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

def create_phone(request):
    # p = Phone(name= 'the queen')
    # p.save()
    return HttpResponse(f'Time {datetime.time}')

def test_page(request):
    return HttpResponse("Hello world!")

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    template_name = "details.html"
    context = {"product": product}
    return render(request, template_name, context)
