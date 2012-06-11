__author__ = 'caleb'

from django.conf.urls import patterns, include, url

from projects import views


urlpatterns = patterns('',
    url(r'^create/$',
        views.create_project,
        name='create_project'),
    url(r'^edit/$',
        views.edit_project,
        name='edit_project'),
    url(r'^/$',
        views.project_detail,
        name='project_detail'),
    url(r'^success/$',
        views.project_creation_success,
        name='success'),
    url(r'^search_project$', views.search_project, name="project_search" )
    )


