import time

from django.http import HttpResponse
from django.shortcuts import render_to_response

import eventlet
from eventlet.green import urllib2

urls = ["http://blog.e0ne.info/themes/darkblog/noavatar.jpg",
     "http://blog.e0ne.info/images/qrcode.png",
     "http://blog.e0ne.info/themes/darkblog/images/rss.jpg"]

def fetch(url):
    return urllib2.urlopen(url).read()

def index(request):
    return render_to_response('index.html')

def updates(request):
    length = 0
    pool = eventlet.GreenPool()
    for body in pool.imap(fetch, urls):
        length+=len(body)
    time.sleep(3)
    return HttpResponse(length)