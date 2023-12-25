from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('delete/', delete_qr_code, name="delete"),
    path('gift/<str:qr_hash>/', congrats)
]