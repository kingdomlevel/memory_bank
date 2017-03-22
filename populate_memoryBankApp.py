import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'memory_bank.settings')

import django
django.setup()
from memoryBankApp.models import List, ListItem, BankItem, EnhancedList
from django.contrib.auth.models import User

def populate():


    #  create lists of dictionaries containing items and lists
    shopping_items = [
        {"title": "Beans"},
        {"title": "Noodles"},
        {"title": "lager"}]

    college_items = [
       {"title": "learn binary search trees"},
       {"title": "pass all exams"},
       {"title": "go for a pint"}]

    lists = {"Shopping": {"items": shopping_items},
             "College": {"items": college_items}}

    elists = {"I-tech Paper", "Algorithm Notes", "Cyber Security"}

    blists = {"Beans", "Noodles", "Lager", "Internet Technology",
              "Algorithms", "Advanced Programming"}

    for list, list_data in lists.iteritems():
        l = add_list(list, 1)
        for i in list_data["items"]:
            add_item(l, i["title"])

    for l in List.objects.all():
        for i in ListItem.objects.filter(list=l):
            print("- {0} - {1}".format(str(l), str(i)))

    for elist in elists:
        add_enhanced(elist, 1)

    for blist in blists:
        add_bank_item(blist, 1)



def add_item(list, title):
    i = ListItem.objects.get_or_create(list=list, title=title)[0]
    i.save()
    return i

def add_list(title, user_id):
    l=List.objects.get_or_create(title=title, user_id=user_id)[0]
    l.save()
    return l

def add_enhanced(title, user_id):
    e=EnhancedList.objects.get_or_create(title=title, user_id=user_id)[0]
    e.save()
    return e

def add_bank_item(title, user_id):
    b=BankItem.objects.get_or_create(title=title, user_id=user_id)[0]
    b.save()
    return b

def add_mike():
    user = User.objects.create_user(
        username='mike',
        password='P@ssword',
        email='mike@mike.com',
        first_name='mike',
        last_name='teller'
    )
    user.save()


if __name__ == '__main__':
    print("Starting memory bank pop script..")
    populate()
























