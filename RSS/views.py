from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse
import urllib.request
import cgi
import feedparser
def index(request):  
	template = loader.get_template('index.html') 
     # getting our template  
	return HttpResponse(template.render())       
     # rendering the template in HttpResponse 
def greetings(request):
        urlname = request.GET["urlname"]
        feed = feedparser.parse(urlname)
        #feed_title = feed['feed']['title']
        feed_entries = feed.entries
  #      for elem in feed_entries:
   #        print (elem.get("published"))
        return render(request, 'news.html', {"urlname": feed_entries})
