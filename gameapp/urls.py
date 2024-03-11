
from django.contrib import admin
from django.urls import path
from gameapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('collection/',views.collection),
]
