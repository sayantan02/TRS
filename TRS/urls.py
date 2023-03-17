from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', include("frontend.urls")),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('students/', include("students.urls")),
    path('payments/', include("payments.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
