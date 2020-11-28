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

# Create your views here.
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

def generate_model_custom(request):
    if request.user.is_authenticated:
        # data = pd.read_csv(os.path.join(BASE_DIR, 'tf_idf/models/Papers Data.csv'),encoding='latin1')  

        # for idx, row in data.iterrows():
        #     exists = Papers.objects.filter(paper_id=row[0]).exists() # return True/False
        #     if not exists:
        #         author_keywords = row[2]
        #         abstract = row[3]
        #         # documents.append(abstract)
        #         _, created = Papers.objects.get_or_create(
        #             paper_id=row[0],
        #             paper_title=row[1],
        #             author_keywords=author_keywords,
        #             abstract=abstract,
        #             area=row[4],
        #         )
        
        documents = []
        papers = Papers.objects.all()
        for paper in papers:
            document = paper.paper_title + " " + paper.abstract
            documents.append(document)

        uniquewords = []
        for doc in documents:
            parsed_doc = doc.split(' ')
            uniquewords = set(parsed_doc).union(set(uniquewords))

        wordsCountDict = []
        tfDict = []
        for idx, doc in enumerate(documents):
            parsed_doc = doc.split(' ')
            numOfWords = dict.fromkeys(uniquewords, 0)
            for word in parsed_doc:
                numOfWords[word] += 1
            wordsCountDict.append(numOfWords);
            tf = computeTF(numOfWords, parsed_doc)
            tfDict.append(tf)

        idfs = computeIDF(wordsCountDict)

        for tf in tfDict:
            tfIdf = computeTFIDF(tf, idfs)

        # 3: User Query
        paper_title = request.GET.get('paper_title')
        keywords = request.GET.get('keywords')
        abstract = request.GET.get('abstract')
        area = request.GET.get('area')

        queryDocument = paper_title + " " + abstract
        
        parsed_doc = queryDocument.split(' ')
        queryNumOfWords = dict.fromkeys(uniquewords, 0)
        for word in parsed_doc:
            queryNumOfWords[word] += 1

        wordsCountDict = [queryNumOfWords]
        tfDict = computeTF(queryNumOfWords, parsed_doc)
        print(tfDict)

        Idfs = computeIDF(wordsCountDict)

        queryTfIdf = computeTFIDF(tfDict, Idfs)
        print(queryTfIdf)

        return render(request, 'search.html')
    else:
        return redirect('/login')

def search_articles(request):
    if request.user.is_authenticated:
        paper_title = request.GET.get('paper_title')
        keywords = request.GET.get('keywords')
        abstract = request.GET.get('abstract')
        area = request.GET.get('area')
        print("tf_idf ->", paper_title, keywords, abstract, area)
        
        return render(request, 'search.html')
    else:
        return redirect('/login')