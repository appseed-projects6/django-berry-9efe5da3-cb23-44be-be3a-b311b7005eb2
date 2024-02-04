# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Prescriptionproperty(models.Model):

    #__Prescriptionproperty_FIELDS__
     property_name = models.CharField(max_length=255, null=True, blank=True)

    #__Prescriptionproperty_FIELDS__END

    class Meta:
        verbose_name        = _("Prescriptionproperty")
        verbose_name_plural = _("Prescriptionproperty")


class Lenstype(models.Model):

    #__Lenstype_FIELDS__
    lenstype = models.CharField(max_length=255, null=True, blank=True)

    #__Lenstype_FIELDS__END

    class Meta:
        verbose_name        = _("Lenstype")
        verbose_name_plural = _("Lenstype")



#__MODELS__END
