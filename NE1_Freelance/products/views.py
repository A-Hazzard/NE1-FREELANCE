from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def dynamic_lookup_view(request, my_id):
    ob = Product.objects.get(id = my_id)

    context = {
        "object":ob
    }
    return render(request, 'products/detail.html', context)








# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'price': obj.price
#     }
#     return render(request, 'product_detail.html', context)

# def product_create_view(request):
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             createProduct = Product.objects.create(**form.cleaned_data)
#             product = Product.objects.get(id= 5)
#             print("The first product is: ", product.title)
#         else:
#             print(form.errors)
#     else:
#         form = RawProductForm(request.GET)

#     context = {
#         "form": form
#     }
    
#     return render(request, 'products/product_create.html', context)


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