from django.urls import path
from . import views

urlpatterns = [
    # website pages URLs
    path('', views.home), path('home/', views.home),
    path('login_page/', views.login_page),
    path('register_page/', views.register_page),
    path('search_page/', views.search_page),

    # website actions URLs
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
