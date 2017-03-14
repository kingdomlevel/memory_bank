from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    max = 128
    #id = models.IntegerField(primary_key=True)

    #may need to add 'unique=True' to the title parameters if
    #we have issues
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=max)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #slug = models.SlugField(unique=True)

  #  def save(self,*args, **kwargs):
     #   self.slug = slugify(self.title)
    #    super(List,self).save(*args, **kwargs)

    #class Meta:
     #   verbose_name_plural = 'lists'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


class ListItem(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    max = 128
    title = models.CharField(max_length=max)
    date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length = 30, null=True, blank=True)
    notes_max = 999
    notes = models.CharField(max_length=notes_max, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)


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




