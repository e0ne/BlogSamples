from django.shortcuts import render_to_response
import django.template.context

from minidetector import detect_mobile

@detect_mobile
def index(request):
    return render_to_response('index.html', context_instance=django.template.context.RequestContext(request))