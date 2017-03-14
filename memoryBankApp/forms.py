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
    title = forms.CharField(max_length=ListItem.max, help_text="Please give your item a title")
    #include a javascript datepicker for the date field
    priority_list = [(1,'low'), (2,'medium'), (3,'high')]
    priority = forms.ChoiceField(choices=priority_list, help_text="How important is this?")
    notes = forms.CharField(widget=forms.Textarea, max_length=ListItem.notes_max, help_text="Any additional information?")
    date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = ListItem
        fields = ('title', 'priority', 'notes', 'date', ) #'priority', 'notes',)


class EditItemForm(forms.ModelForm):
    title = forms.CharField(max_length=ListItem.max, help_text="Change Title?")
    #include a javascript datepicker for the date field
    priority_list = [(1,'low'), (2,'medium'), (3,'high')]
    priority = forms.ChoiceField(choices=priority_list, help_text="How important is this?")
    notes = forms.CharField(widget=forms.Textarea,max_length=ListItem.notes_max, help_text="Any additional information?")
    date = forms.DateField(widget=forms.SelectDateWidget)
    completed = forms.BooleanField(label="Mark as Completed:", required=False)
    removed = forms.BooleanField(label= "Mark for Deletion:", required=False)
    class Meta:
        model = ListItem
        fields = ('title', 'date', 'priority', 'notes', 'completed','removed',) #'priority', 'notes',)
