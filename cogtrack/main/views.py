# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#from django import oldforms as forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm


def index(request):
  template = loader.get_template('index.html')
  context = Context({
      'user': request.user,
  })
  return HttpResponse(template.render(context))

def tests_index(request):
  template = loader.get_template('tests/index.html')
  context = Context({
      'user': request.user,
  })
  return HttpResponse(template.render(context))

def signup(request):
  form = UserCreationForm()

  if request.method == 'POST':
    data = request.POST.copy()
    errors = form.get_validation_errors(data)
    if not errors:
      new_user = form.save(data)
      return HttpResponseRedirect("/")
  else:
    data, errors = {}, {}

  return render_to_response("signup.html", {
    'form' : forms.FormWrapper(form, data, errors)
  })