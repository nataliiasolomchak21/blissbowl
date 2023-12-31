from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def all_products(request):
    """ 
    A view to return the products page
    """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:    
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.info(request, f"Sorry, nothing found for '{query}'.")
        
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'selected_category': request.GET.get('category'),  # Add this line to pass the selected category
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show product details of each product 
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)