from django.conf.urls import url
from memoryBankApp import views

# this tuple creates an individual URL mapping. it MUST be called urlpatterns
# '^$' is a regular expression for empty String
#  Any URL supplied by the user that matches this pattern means that the view
#  views.index() would be invoked by Django
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'contact/', views.contact, name='contact'),
    url(r'faq/', views.faq, name='faq'),
    url(r'^list/(?P<id>\d+)/$', views.edit_item, name='edit_item'),
    url(r'^home/$', views.home, name='home'),
    url(r'^enhancedlist/$', views.enhancedlist, name='enhancedlist'),
    url(r'^enhancedlist/(?P<id>\d+)/$', views.edit_enhanced_list, name='edit_enhanced_list'),
	url(r'^quick_item/$', views.quick_item, name='quick_item'),
    url(r'^update_list/$', views.update_list, name='update_list'),

]
