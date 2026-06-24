from django.shortcuts import render
from .models import GalleryImage


def gallery(request):
    images = GalleryImage.objects.filter(is_active=True)

    return render(request, 'gallery/gallery.html', {
        'images': images
    })
