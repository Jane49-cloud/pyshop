from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse("New products")


def goods(request):
    return HttpResponse("These are all the goods.")


def contact(request):
    return render(request, 'contact.html',
                  {'products': contact})





