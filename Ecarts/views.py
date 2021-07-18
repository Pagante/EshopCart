from django.shortcuts import render
from store.models import Product, BestProduct, TrendingProduct

def home(request):
    products = Product.objects.all().filter(is_available=True)
    bestProduct = BestProduct.objects.all().filter(is_available=True)
    trendProducts = TrendingProduct.objects.all().filter(is_available=True)

    context = {
        'products' : products,
        'bestProduct' : bestProduct,
        'trendProducts': trendProducts,
    }
    return render(request, 'home.html', context)