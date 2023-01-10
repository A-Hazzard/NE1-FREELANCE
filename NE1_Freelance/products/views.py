from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'price': obj.price
    }
    return render(request, 'product_detail.html', context)

def product_create_view(request):
    form = ProductForm(request.Post or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'product_create.html', context)