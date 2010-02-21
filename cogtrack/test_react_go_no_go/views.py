# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from cogtrack.test_react_go_no_go.models import GoNoGo

def index(request):
  results_list = GoNoGo.objects.all().order_by('-reaction_time')[:10]
  template = loader.get_template('tests/go_no_go/index.html')
  context = Context({
      'results_list': results_list,
  })
  return HttpResponse(template.render(context))
