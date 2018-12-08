from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TechProduct, TechReview

# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')

def getProducts(request):
    product_list=TechProduct.objects.all()
    return render(request, 'reviews/products.html', {'product_list': product_list} )

def productdetail(request, id):
    product=get_object_or_404(TechProduct, pk=id)
    return render(request, 'reviews/productdetail.html',{'product' : product})

def productreviews(request, prod_id):
    prodreveiws=TechReview.objects.filter(product=prod_id)
    return render(request, 'reviews/productreview.html', {'prodreviews': prodreveiws})

