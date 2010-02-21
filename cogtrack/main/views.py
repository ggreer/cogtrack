# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
  template = loader.get_template('index.html')
  context = Context({
      'user': request.user,
  })
  return HttpResponse(template.render(context))

