from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

import math

from cogtrack.cogtest.models import CogTest
from cogtrack.test_react_go_no_go.models import GoNoGo

def index(request):
  results_list = GoNoGo.objects.all().order_by('end')[:10]

  chart_urls = []
  max_reaction_time = 0
  data_string = ""
  chart_url = "http://chart.apis.google.com/chart?chtt=Reaction Time&cht=lc&chxt=x,y,y&chs=500x250&chd=t:"

  for result in results_list:
    max_reaction_time = max(max_reaction_time, result.reaction_time)
    data_string += "%u," % result.reaction_time
    label_string += ""

  max_reaction_time = math.ceil(float(max_reaction_time)/100) * 100
  chart_url += data_string[:-1]
  chart_url += "&chds=0,%u&chxr=1,0,%u&chxl=0:|2009|2010|2:|Milliseconds&chxp=0,5|2,50" % (max_reaction_time, max_reaction_time)
  chart_urls.append(chart_url)

  data_string = ""
  chart_url = "http://chart.apis.google.com/chart?chtt=Error Rate&cht=lc&chxt=x,y&chs=500x250&chds=0,20&chd=t:"
  for result in results_list:
    data_string += '%f,' % (float(result.errors) / result.tests)

  chart_url += data_string[:-1]
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
