from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class List(models.Model):
    max = 128
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=max)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    removed = models.BooleanField(default=False)

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
    notes_max = 999
    notes = models.CharField(max_length=notes_max, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)


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
    bank = models.ForeignKey(Bank, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class EnhancedList(models.Model):
    title_max = 128
    long_text_max = 9999
    title = models.CharField(max_length=title_max)
    long_text = models.CharField(max_length=long_text_max, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.title)
