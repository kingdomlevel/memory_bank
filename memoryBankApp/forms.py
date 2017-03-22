from django import forms
from memoryBankApp.models import List, ListItem, EnhancedList
from datetime import date


class ListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}), max_length=List.max,
                            help_text="Please give your list a name.")

    class Meta:
        model = List
        fields = ('title',)


class ListItemForm(forms.ModelForm):
    # title = forms.CharField(max_length=ListItem.max, help_text="Please give your item a title",
    #                         widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    priority_list = [(1,'low'), (2,'medium'), (3,'high')]
    priority = forms.ChoiceField(choices=priority_list, help_text="How important is this?")
    notes = forms.CharField(widget=forms.Textarea, max_length=ListItem.notes_max,
                            help_text="Any additional information?", required=False)
    date = forms.DateField(widget=forms.SelectDateWidget, initial=date.today,)
    class Meta:
        model = ListItem
        fields = ( 'date', 'priority', 'notes',)


class EditItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}),
                            max_length=ListItem.max, help_text="Change Title?", label="Title: ")
    priority_list = [(1,'low'), (2,'medium'), (3,'high')]
    priority = forms.ChoiceField(choices=priority_list, help_text="How important is this?", label="Priority Level: ")
    notes = forms.CharField(widget=forms.Textarea,max_length=ListItem.notes_max,
                            help_text="Any additional information?", label="Notes: ", required=False)
    date = forms.DateField(widget=forms.SelectDateWidget, initial=date.today, label="Due date: ")
    completed = forms.BooleanField(label="Mark as Completed:", required=False)
    # removed = forms.BooleanField(label= "Mark for Deletion:", required=False)
    class Meta:
        model = ListItem
        fields = ('title', 'date', 'priority', 'notes', 'completed',)


class EnhancedListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}),
                            max_length=EnhancedList.title_max, label="Title: ")
    #long_text = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = EnhancedList
        fields = ('title', 'long_text',)


class DeleteListForm(forms.ModelForm):
    title = forms.CharField(max_length=List.max)

    class Meta:
        model = List
        fields = ('title', )


class QuickItemForm(forms.Form):
    title = forms.CharField(max_length=ListItem.max, required='True')
