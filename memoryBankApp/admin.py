from django.contrib import admin
from memoryBankApp.models import List, ListItem

#class ListAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(List)
admin.site.register(ListItem)