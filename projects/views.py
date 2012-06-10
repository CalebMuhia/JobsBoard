# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import context
from django.template.context import RequestContext
from projects.models import Projects, ProjectForm


def create_project(request,):

    if request.method == 'POST':
        formset = ProjectForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('success'))

    else:
        formset = ProjectForm()
    return render_to_response("projects/create_projects.html", {
        "formset": formset,

        }, context_instance = RequestContext(request))
create_project = login_required(create_project)



def edit_project(request):
    pass


def project_detail(request):
    pass


def project_creation_success(request):
    return render_to_response('projects/success.html')