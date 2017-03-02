from django import forms
from memoryBankApp.models import List, ListItem, Bank, BankItem
from django.contrib.auth.models import User

class ListForm(forms.ModelForm):
    title = forms.CharField(max_length=List.max)

    class Meta:
        model = List
        fields = ('title',)