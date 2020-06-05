from django.contrib import admin

#importowanie funkcji path Django i views z app blog

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
]