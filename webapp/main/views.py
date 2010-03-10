from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

def index(request):
  return render_to_response('index.html', {}, context_instance = RequestContext(request))

def about(request):
  return render_to_response('about.html', {}, context_instance = RequestContext(request))

def tests_index(request):
  return render_to_response('tests/index.html', {}, context_instance = RequestContext(request))

def signup(request):
  form = UserCreationForm()

  if request.method == 'POST':
    data = request.POST.copy()

    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect(START_PAGE)
    else:
      form = UserCreationForm()

  return render_to_response("signup.html", { 'form' : form }, context_instance = RequestContext(request))