from django import forms
from memoryBankApp.models import List, ListItem, Bank, BankItem
from django.contrib.auth.models import User

class ListForm(forms.ModelForm):
    title = forms.CharField(max_length=List.max,
                            help_text="Please give your list a name.")

    class Meta:
        model = List
        fields = ('title',)


class ListItemForm(forms.ModelForm):
    title = forms.CharField(max_length=ListItem.max)
    #include a javascript datepicker for the date field
    #priority_list = ['low', 'medium', 'high']
    priority = forms.ChoiceField(choices=('low', 'medium', 'high'))
    notes = forms.CharField(max_length=ListItem.notes_max)

    class Meta:
        model = ListItem
        fields = ('title', 'priority', 'notes',) #'priority', 'notes',)

