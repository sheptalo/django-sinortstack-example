from django.contrib import admin
from django.urls import path
from ..api.users import register

urlpatterns = [
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
]

