from django.shortcuts import render, redirect
from .models import Photo, Category
from .forms import ImageUploadForm

# Create your views here.
def gallery(request):

    category = request.GET.get('category')

    if category == None:
        images = Photo.objects.all()
    else:
        images = Photo.objects.filter(category__name=category)

    master_categories = Category.objects.all()

    context = {'images': images, 'master_categories': master_categories}

    return render(request, 'photo_app/gallery.html', context)


def bulk_upload(request):
    
    context = {}

    return render(request, 'photo_app/bulk_upload.html', context)


def upload_photo(request):

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/gallery')

    else:
        form = ImageUploadForm()

    context = {'form': form}

    return render(request, 'photo_app/upload_photo.html', context)


def view_photo(request, pk):

    image = Photo.objects.get(id=pk)

    context = {'image': image}

    return render(request, 'photo_app/photo.html', context)

