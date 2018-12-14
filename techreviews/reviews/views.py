from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TechProduct, TechReview
from .forms import TechProductForm, TechReviewForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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

@login_required
def newProduct(request):
    form=TechProductForm

    if request.method=='POST':
        form=TechProductForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=TechProductForm()
    else:
        form=TechProductForm()
    return render(request, 'reviews/newproduct.html', {'form': form})

@login_required
def newReview(request):
    form=TechReviewForm

    if request.method=='POST':
        form=TechReviewForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=TechReviewForm()
    else:
        form=TechReviewForm()
    return render(request, 'reviews/newreview.html', {'form': form})

def logoutmessage(request):
    return render(request, 'reviews/logoutmessage.html')

def loginmessage(request):
    return render(request, 'reviews/loginmessage.html')