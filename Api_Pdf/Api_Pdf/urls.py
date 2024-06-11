from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls

from post.api.router import router_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_posts.urls)),
    path('docs/', include_docs_urls(title= 'Api Documentation')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
