from django.contrib import admin
from django.urls import path
from twilight import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', views.webhook),
)
