from django.urls import path
from .views import home, ImageUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('api/upload/', ImageUploadView.as_view(), name='image-upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
