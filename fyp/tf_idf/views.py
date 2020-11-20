from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.contrib.auth.models import User, auth

# Create your views here.

def search_articles(request):
    if request.user.is_authenticated:
        paper_title = request.GET.get('paper_title')
        keywords = request.GET.get('keywords')
        abstract = request.GET.get('abstract')
        print("tf_idf ->", paper_title, keywords, abstract)
        
        return render(request, 'search.html')
    else:
        return redirect('/login')