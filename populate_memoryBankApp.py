import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'memory_bank.settings')

import django
django.setup()
from memoryBankApp.models import List, ListItem

def populate():

    #  create lists of dictionaries containing items and lists
    shopping_items = [
        {"title": "Beans"},
        {"title": "Noodles"},
        {"title": "lager"}]

  #  college_items =[
   #     {"title:" "learn binary search trees"},
    #    {"title:" "pass all exams"},
     #   {"title:" "go for a pint"}]

    lists = {"Shopping": {"items": shopping_items}}
           # "College": {"items": college_items}}

    for list, list_data in lists.iteritems():
        l = add_list(lists)
        for i in list_data["items"]:
            add_item(l, i["title"])

    for l in List.objects.all():
        for i in ListItem.objects.filter(list=l):
            print("- {0} - {1}".format(str(l), str(i)))


def add_item(list, title):
    i = ListItem.objects.get_or_create(list=list, title=title)[0]
    i.save()
    return i

def add_list(title):
    l=List.objects.get_or_create(title=title)[0]
    l.save()
    return l

if __name__ == '__main__':
    print("Starting memory bank pop script..")
    populate()
























