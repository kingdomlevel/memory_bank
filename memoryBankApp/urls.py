from django.conf.urls import url
from memoryBankApp import views

# this tuple creates an individual URL mapping. it MUST be called urlpatterns
# '^$' is a regular expression for empty String
#  Any URL supplied by the user that matches this pattern means that the view
#  views.index() would be invoked by Django
urlpatterns = [
    # public site admin
    url(r'^$', views.index, name='index'),

    url(r'^testlist/$', views.testlist, name='testlist'),
    url(r'about/', views.about, name='about'),
    url(r'contact/', views.contact, name='contact'),
    url(r'faq/', views.faq, name='faq'),
    url(r'^testform/$', views.testform, name='testform'),
    url(r'^testitemform/$', views.testitemform, name='testitemform'),
    url(r'^list/(?P<id>\d+)/$', views.edit_item, name='edit_item'),
    url(r'^home/$', views.home, name='home'),
    url(r'^bankitems/$', views.bank_display, name= 'bank_display'),
    url(r'^banktest/$', views.banktest, name='banktest'),
    url(r'^enhancedlist/$', views.enhancedlist, name='enhancedlist'),
    url(r'^enhancedlist/(?P<id>\d+)/$', views.edit_enhanced_list, name='edit_enhanced_list'),
    # url(r'about/', views.about, name='about'),
    # url(r'contact/', views.contact, name='contact'),
    # url(r'faq/', views.faq, name='faq'),


    # # user acccount stuff no longer necessary -NOTE - This should now be handled with registration Redux
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),


    # url(r'^settings/$', views.settings, name='settings'),
    #
    # # user's personalised pages

    # url(r'^new-list/$', views.new_list, name='new_list'),
    # url(r'^create-bank/$', views.create_bank, name='create_bank'),
    # # ?? DO WE ACTUALLY NEED THE BELOW URL??
    # # replace w scripting?
    # url(r'^list/(?P<list_name_slug>[\w\-]+)/$', views.list, name='list'),
    # # ?? DO WE ACTUALLY NEED THE BELOW URL??
    # # replace w scripting?
    # url(r'^list/(?P<list_name_slug>[\w\-]+)/add-item/$', views.add_item,
    #     name='add_item'),
    # url(r'^list/(?P<list_name_slug>[\w\-]+)/(?P<item_name_slug>[\w\-]+)/$',
    #     views.item, name='item'),
]
