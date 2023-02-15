from django.shortcuts import render
from .models import AboutUsContent
from .forms import ImageForm

def aboutus(request):
    information = AboutUsContent.objects.get(id=1)
    return render(request,'aboutus/aboutus.html', {'information':information})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})