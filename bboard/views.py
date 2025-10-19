import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from bboard.models import Phone

def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.all()
    template = 'product.html'
    context = {"phones": phones}
    return render(request, template, context)

def time(request):
    return HttpResponse(f'Time {datetime.datetime.now()}')