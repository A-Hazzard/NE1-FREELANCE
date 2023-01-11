from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def dynamic_lookup_view(request, id):

    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        raise Http404
        
    context = {
        "product":product
    }

    return render(request, 'products/detail.html', context)

def delete_product_view(request, id):

    try:
        product = get_object_or_404(Product, id = id)

        if request.method == 'POST':
            product.delete()
            return redirect('../../')

        context = {
            "product": product
        }
        return render(request, 'products/product_delete.html', context)

    except Product.DoesNotExist:
        raise Http404

def deleteProducts_view(request):

    return render(request, 'products/delAllProducts.html', {})


def deleteProducts(request):

    Product.objects.all().delete()

    return render(request, 'products/clearedDb.html', {})


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'price': obj.price
#     }
#     return render(request, 'product_detail.html', context)

def product_create_view(request):
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            createProduct = Product.objects.create(**form.cleaned_data)
            product = Product.objects.get(id= createProduct.id)
            print("Product: ", product.id)
        else:
            print(form.errors)
    else:
        form = RawProductForm(request.GET)

    context = {
        "form": form
    }
    
    return render(request, 'products/product_create.html', context)


# def product_create_view(request):

#     if request.method == 'POST':
#         form = ProductForm(request.POST)

#         if form.is_valid():
#             form.save()
#             form = ProductForm()

        
#     else:
#         form = ProductForm()

#     context = {
#             'form': form
#         }
        
#     return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     context = {}
#     print('GET requested: ', request.GET)
#     print('\n')
#     print('POST requested: ', request.POST)
#     return render(request, "products/product_create.html", context)