from django.shortcuts import render
from news.models import News
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.

def index(request):
    news = []
    for item in News.objects.all():
        news.append({
            'id':item.id,
            'title':item.title,
            'content':item.content,
            'image':item.image.url,
            'date':item.date,
            'source':item.source,
            'writer':'%s %s'%(item.created_by.first_name, item.created_by.last_name)
        })

    paginator = Paginator(news, settings.NEWS_PAGE_SIZE) # Show 25 contacts per page

    page = request.GET.get('page')
    news = paginator.get_page(page)

    return render(request, 'news_all.html', {'news': news})

def RetrivNews(request):
    news = []
    try:
        news_type = request.GET.get('type', None)
        id = request.GET.get('id', None)
        if id !=  None:
            obj = News.objects.filter(id=id)[0]
            news.append({'writer':obj.get_writer(),
                   'content':obj.content,
                   'image':obj.image.url,
                   'title':obj.title})
            return render(request,'news_one.html',{'news':news})

        if news_type=='iran':
            items = News.objects.filter(international=False)
        elif news_type=='international':
            items = News.objects.filter(international=True)
        else:
            items = News.objects.all()

        for item in items:
            news.append({
                'id':item.id,
                'title':item.title,
                'content':item.content,
                'image':item.image.url,
                'date':item.date,
                'source':item.source,
                'writer':'%s %s'%(item.created_by.first_name, item.created_by.last_name)
            })

        paginator = Paginator(news, settings.NEWS_PAGE_SIZE) # Show 25 contacts per page

        page = request.GET.get('page')
        news = paginator.get_page(page)

        return render(request, 'news_all.html', {'news': news})

    except:
        return render(request,'404.html')

def RetriveNewsById(request):
    if request.method=='GET':
        try:
            news = News.objects.first(id=request.GET['id'])
            return render(request, 'news_one.html',{'news':news})
        except:
            return render('404.html')
    else:
        return render('404.html')