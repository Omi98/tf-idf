from django.urls import path
from . import views

urlpatterns = [
    # website pages URLs
    
    # website actions URLs
    path('api/search_articles/', views.search_articles)
]
