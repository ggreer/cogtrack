from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from cogtrack.cogtest.models import CogTest
from cogtrack.test_react_go_no_go.models import GoNoGo

def index(request):
  chart_urls = []
  results_list = GoNoGo.objects.all().order_by('end')[:10]

  chart_url = "http://chart.apis.google.com/chart?chtt=Reaction Time&cht=lc&chxt=x,y&chs=500x250&chd=t:"
  max_reaction_time = 0
  for result in results_list:
    max_reaction_time = max(max_reaction_time, result.reaction_time)
    chart_url += "%u," % result.reaction_time

  chart_url = chart_url[:-1]
  chart_url += "&chds=0,%u" % max_reaction_time
  chart_urls.append(chart_url)

  chart_url = "http://chart.apis.google.com/chart?chtt=Error Rate&cht=lc&chxt=x,y&chs=500x250&chds=0,20&chd=t:"
  for result in results_list:
    chart_url += '%f,' % (float(result.errors) / result.tests)

  chart_url = chart_url[:-1]
  chart_url += "&chds=0,1"
  chart_urls.append(chart_url)


  template = loader.get_template('tests/go_no_go/index.html')
  context = RequestContext(request, {
      'results_list': results_list,
      'chart_urls': chart_urls,
  })
  return HttpResponse(template.render(context))

def test(request):
  return render_to_response('tests/go_no_go/test.html', {}, context_instance = RequestContext(request))
