from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return self.title
