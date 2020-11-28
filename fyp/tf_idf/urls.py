from django.urls import path
from . import views

urlpatterns = [
    # website pages URLs
    
    # website actions URLs
    path('api/generate_model/', views.generate_model_custom),
    path('api/search_articles/', views.search_articles)
]
