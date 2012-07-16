
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

COUNTRIES = (
    ('fr', ('France')),
    ('de', ('Germany')),

    )


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User , unique=True)
    country = models.CharField(max_length=10, choices=COUNTRIES)
    city = models.CharField(max_length=256)
    zip_code = models.IntegerField(max_length=100, null=True)
    home_address = models.TextField()
    phone_number = models.IntegerField(max_length=10)
    public_profile_field = models.BooleanField(default=True)

    def __str__(self):
        return "%s's profile" % self.user


