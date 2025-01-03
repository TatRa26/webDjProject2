from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('news/', include('news.urls')),
]

# Добавляем обработку статических файлов
if settings.DEBUG:  # Убедимся, что это работает только в режиме отладки
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
