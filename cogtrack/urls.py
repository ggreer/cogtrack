from django.conf.urls.defaults import *
from django.conf import settings

# Enable admin interface
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', 'cogtrack.main.views.index'), # Empty path, show main page.
  (r'^tests/$', 'cogtrack.cogtest.views.index'),
  (r'^tests/go_no_go$', 'cogtrack.test_react_go_no_go.views.index'),
  (r'^tests/go_no_go/test$', 'cogtrack.test_react_go_no_go.views.test'),

  (r'^signup$', 'cogtrack.main.views.signup'),
  (r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
  (r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

  # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
  # to INSTALLED_APPS to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  
  # Uncomment the next line to enable the admin:
  (r'^admin/', include(admin.site.urls)),
)

# Allow Django to serve static files so that mongoose isn't needed for development
if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
