from django.forms import forms

__author__ = 'caleb'



class SearchForm(forms.Form):
    query=forms.CharField(
        label=u'Enter the keyword you would like to search for',
        widget= forms.TextInput(attrs={'size':32})
    )