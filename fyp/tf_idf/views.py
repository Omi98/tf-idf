from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.contrib.auth.models import User, auth

import os
from .settings import BASE_DIR 
import pandas as pd
from .models import Papers
from .models import RecommendationModel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def search_articles(request):
    if request.user.is_authenticated:
        # 3: User Query
        area = request.GET.get('area')
        search = request.GET.get('search')
        keywords = request.GET.get('keywords')
        abstract = request.GET.get('abstract')

        if area is None and search is None and keywords is None and abstract is None:
            return render(request, 'search.html')

        documents = []
        papers = Papers.objects.all()

        papers_docs_mapping = []
        for paper in papers:
            if paper.area == area:
                document = paper.paper_title + " " + paper.abstract + " " + paper.author_keywords
                documents.append(document)
                papers_docs_mapping.append({ 'paper': paper, 'document': document })

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents)

        feature_names = vectorizer.get_feature_names()
        dense = vectors.todense()
        denselist = dense.tolist()


        queryDocument = search + " " + abstract + " " + keywords

        query_vec = vectorizer.transform([queryDocument])

        results = cosine_similarity(vectors,query_vec)

        score_doc_map = [];
        for idx, score  in enumerate(results):
            score_doc_map.append({ 'score': score, 'index': idx })

        score_doc_map.sort(key=lambda x: x['score'], reverse=True)

        sorted_papers = []
        for idx, sorted_doc_idx in enumerate(score_doc_map):
            doc = documents[sorted_doc_idx['index']]
            paper_map = next((item for item in papers_docs_mapping if item["document"] == doc), None)
            score = sorted_doc_idx['score'][0];
            sorted_papers.append({ 'paper': { 'title': paper_map['paper'].paper_title, 'abstract': paper_map['paper'].abstract }, 'score': score, 'id': idx })
            
        return render(request, 'search.html', { 'sorted_papers': sorted_papers, 'area': area, 'total_count': len(sorted_papers) })
    else:
        return redirect('/login')