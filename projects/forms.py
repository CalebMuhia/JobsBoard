from django import forms
from projects.models import Project_categories

__author__ = 'caleb'

class CreateProjectForm(forms.Form):

    title = forms.CharField(
        label=u'Title',
        widget=forms.TextInput(attrs={'size': 64})
    )
    description=forms.CharField(
        label=u'description',
        widget=forms.Textarea()

    )
    budget = forms.CharField(
        label=u'Suggested Budget',
        widget=forms.TextInput(attrs={'size': 64})
    )
    category = forms.ModelChoiceField(queryset=Project_categories.objects.all())
    tags = forms.CharField(
        label=u'Tags',
        required=False,
        widget=forms.TextInput(attrs={'size': 64})
    )

class SearchForm(forms.Form):
    query=forms.CharField(
        label=u'Job Search',
        widget= forms.TextInput(attrs={'size':32})
    )
