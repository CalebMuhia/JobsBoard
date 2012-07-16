# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import context
from django.template.context import RequestContext
from projects.forms import SearchForm, CreateProjectForm
from projects.models import Projects, ProjectForm, Project_categories
from taggit.models import Tag
from timepiece import models as timepiece

@login_required()
def create_project(request,):

    if request.method == 'POST':
        formset = CreateProjectForm(request.POST, request.FILES,)


        if formset.is_valid():

            categories,dummy= Project_categories.objects.get_or_create(
                name= formset.cleaned_data['category']
            )
            projects, created = Projects.objects.filter(

                client_name = request.user,
                category = categories

            )
            projects.title = formset.cleaned_data['title']
            projects.description = formset.cleaned_data['description']
            projects.suggested_budget  = formset.cleaned_data['budget']
            if not created:
                projects.tags.clear()


            # Create new tag list.
            tag_names = formset.cleaned_data['tags'].split()
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                projects.tags.add(tag)

            projects.save()





            return HttpResponseRedirect(reverse('success'))

    else:
        formset = CreateProjectForm()
    return render_to_response("projects/create_projects.html", {
        "formset": formset,'user':request.user

        }, context_instance = RequestContext(request), )
create_project = login_required(create_project)



@login_required()
def edit_project(request):
    pass

@login_required()
def project_detail(request,num):
    num = int(num)
    project = timepiece.Project.objects.get(pk=num)

    return render_to_response('projects/project.html',{'project':project,'user':request.user})

@login_required()
def project_creation_success(request):
    return render_to_response('projects/success.html', {'user':request.user})


@login_required
def search_project(request):
    form=SearchForm()
    projects=[]
    show_results=False
    if 'query' in request.GET:
        show_results=True
        query=request.GET['query'].strip()
        if query:
            form=SearchForm({'query':query})
            projects=Projects.objects.filter(title__icontains=query)[:10]
    if request.GET.has_key('ajax'):
        return render_to_response('projects/projects_list.html', {'form':form,'projects':projects,'show_results':show_results,'show_user':True,'show_tags':True,'user':request.user})
    else:
        return render_to_response('projects/search.html', {'form':form,'projects':projects,'show_results':show_results,'show_user':True,'show_tags':True,'user':request.user})


def search(request):
    form=SearchForm()
    projects=[]
    show_results=False
    if 'query' in request.GET:
        show_results=True
        query=request.GET['query'].strip()
        if query:
            form=SearchForm({'query':query})
            projects=Projects.objects.filter(title__icontains=query)[:10]
    return render_to_response("projects/search_page.html",{'form':form,'projects':projects,'user':request.user})



@login_required()
def dashboard(request):


    categories = timepiece.Project_categories.objects.order_by('name')
    projects = timepiece.Project.objects.order_by('name')

    return render_to_response('index.html',{'categories':categories,'projects':projects,'user':request.user})


def search_options(request):
    return render_to_response("searchoptions.html")

