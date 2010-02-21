from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User
from django.template import RequestContext 
from django.shortcuts import render_to_response

def index(request):
  return render_to_response('tests/index.html', {}, context_instance = RequestContext(request))
