import django.template.context
from django.shortcuts import render_to_response

from microdetector import detect_mobile

@detect_mobile
def index(request):
    #r
    return render_to_response('index.html', context_instance=django.template.context.RequestContext(request))