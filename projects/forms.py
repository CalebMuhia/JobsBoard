from django import forms

__author__ = 'caleb'



class SearchForm(forms.Form):
    query=forms.CharField(
        label=u'Job Search',
        widget= forms.TextInput(attrs={'size':32})
    )
