from django.shortcuts import render
from newsapi import NewsApiClient



def index(request):
    newsapi = NewsApiClient(api_key="cfa38c8065ed4b039cb827db8924d7ee")
    topheadlines = newsapi.get_top_headlines(sources='abc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'index.html', context={"mylist":mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key="cfa38c8065ed4b039cb827db8924d7ee")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'bbc.html', context={"mylist":mylist})
