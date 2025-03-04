from django.urls import path
from infrastructure.api.users import register

urlpatterns = [
	path('register', register, name='register'),
]