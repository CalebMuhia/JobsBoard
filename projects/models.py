from django.db import models
from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
# Create your models here.


from datetime import datetime
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


category = (
    ('programming','Programming'),
    ('article writing','Article'),
)
class Project_categories(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')

class Projects(models.Model):
    title = models.CharField(max_length=100,blank=False)
    client_name= models.ForeignKey(User)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.now)
    tags = TaggableManager()
    suggested_budget = models.CharField(max_length=100)
    category =models.ForeignKey(Project_categories)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')



class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ('title','description','date_created','tags','suggested_budget','category')



class ProjectCategoryForm(ModelForm):
    class Meta:
        model = Project_categories



