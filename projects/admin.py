__author__ = 'caleb'

from django.contrib import admin
from projects.models import *
admin.site.register(Project_categories)
admin.site.register(Projects)