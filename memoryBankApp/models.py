from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class List(models.Model):
    max = 128
    #id = models.IntegerField(primary_key=True)

    #may need to add 'unique=True' to the title parameters if
    #we have issues
    title = models.CharField(max_length = max)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class ListItem(models.Model):
    max = 128
    title = models.CharField(max_length = max)
    date = models.DateField()
    priority = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)
    notes = models.CharField(max_length = 999)
    list = models.ForeignKey(List)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Bank(models.Model):
    max = 128
    title = models.CharField(max_length=max)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class BankItem(models.Model):
    max = 128
    title = models.CharField(max_length=max)
    bank = models.ForeignKey(Bank)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



