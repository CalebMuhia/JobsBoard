import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from schoolproject import settings

admin.autodiscover()
static = os.path.join(
    os.path.dirname(__file__), 'static'
)

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'projects.views.dashboard', name='home'),
    # url(r'^schoolproject/', include('schoolproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^projects/', include('projects.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^timepiece/', include('timepiece.urls')),
    (r'^selectable/', include('selectable.urls')),

)
