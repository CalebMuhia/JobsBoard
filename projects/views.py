# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import context
from django.template.context import RequestContext
from projects.models import Projects, ProjectForm, Project_categories
from taggit.models import Tag

@login_required()
def create_project(request,):

    if request.method == 'POST':
        formset = ProjectForm(request.POST, request.FILES,)

        if formset.is_valid():


            project,created = Projects.objects.get_or_create(
                client_name= request.user,
                category = formset.cleaned_data['category']
            )
            project.title = formset.cleaned_data['title']
            project.description = formset.cleaned_data['description']
            project.date_created = formset.cleaned_data['date_created']
            project.suggested_budget = formset.cleaned_data['suggested_budget']


            if not created:
                project.tags.clear()

            # Create new tag list.
            tag_names = formset.cleaned_data['tags']
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                project.tags.add(tag)

            project.save()
            return HttpResponseRedirect(reverse('success'))

    else:
        formset = ProjectForm()
    return render_to_response("projects/create_projects.html", {
        "formset": formset,'user':request.user

        }, context_instance = RequestContext(request), )
create_project = login_required(create_project)


@login_required()
def edit_project(request):
    pass

@login_required()
def project_detail(request):
    pass

@login_required()
def project_creation_success(request):
    return render_to_response('projects/success.html', {'user':request.user})