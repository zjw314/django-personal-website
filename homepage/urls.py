#homepage/urls.py

from django.urls import path
from .views import PWMainView

urlpatterns = [
    path('', PWMainView.as_view(), name='home'),
]
