from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category
# Create your views here.

def products(request):
    product = Product.objects.all()
    product_json = [product.to_json() for product in product]
    return JsonResponse(product_json, safe=False)
def product_id(request, product_id):
    product = Product.objects.get(id=product_id)
    return JsonResponse(product.to_json(), safe=False)

def categories(request):
    category = Category.objects.all()
    category_json = [category.too_json() for category in category]
    return JsonResponse(category_json, safe=False)
def categories_id(request, categories_id):
    categories = Category.objects.get(id=categories_id)
    return JsonResponse(categories.too_json(), safe=False)


