from django.shortcuts import render

# Create your views here.
def gallery(request):

    context = {}

    return render(request, 'photo_app/gallery.html', context)


def bulk_upload(request):
    
    context = {}

    return render(request, 'photo_app/bulk_upload.html', context)


def upload_photo(request):
    
    context = {}

    return render(request, 'photo_app/upload_photo.html', context)


def view_photo(request):
    
    context = {}

    return render(request, 'photo_app/photo.html', context)

