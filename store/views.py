from django.core import paginator
from django.shortcuts import render,get_object_or_404
from .models import Product, TrendingProduct,BestProduct
from category.models import Category
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug !=None:
        categories =get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)

        product_count = products.count()

    context = {
        'products':paged_product,
        'product_count':product_count,
    }
    return render(request, 'store/store.html',context)



def product_detail(request, category_slug, product_slug):
    try:
        categories = None
        products = None

        if category_slug !=None:
            categories =get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=categories, is_available=True)
            trendProducts = TrendingProduct.objects.all().filter(is_available=True)
            # trendProducts = TrendingProduct.objects.filter()
            single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        else:
            trendProducts = TrendingProduct.objects.all().filter(is_available=True)

    except Exception as e:
        raise e

    context = {
        'single_product':single_product,
        'products':products,
        'trendProducts':trendProducts,
    }
    return render(request, 'store/single_product.html', context)




def search(request):
    products = None
    productCounts=None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword)).distinct()
            productCounts = products.count()

    context = {
        'products':products,
        'productCounts': productCounts,
    }
    return render(request, 'store/store.html', context)

