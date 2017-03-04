from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from memoryBankApp.forms import ListForm
from memoryBankApp.models import List, ListItem




# Create your views here.


def index(request):
	# request.session.set_test_cookie()

	# category_list = Category.objects.order_by('-likes')[:5]
	# page_list = Page.objects.order_by('-views')[:5]
	# context_dict = {'categories': category_list, 'pages': page_list}

	# visitor_cookie_handler(request)
	# context_dict['visits'] = request.session['visits']


	response = render(request, 'memoryBankApp/index.html')
	return response

def home(request):
	allLists = List.objects.all()
	context_dict = {'allLists': allLists,}
	return render(request, 'memoryBankApp/home.html', context_dict)


def testlist(request):
	list1 = List.objects.get(pk=1)
	list2 = List.objects.get(pk=2)
	context_dict = {'list1': list1, 'list2': list2 }
	return render(request, 'memoryBankApp/testlist.html', context_dict)


def about(request):
	print(request.method)
	return render(request,'memoryBankApp/about.html',{})

def faq(request):
	print(request.method)
	return render(request, 'memoryBankApp/faq.html', {})

def contact(request):
	print(request.method)
	return render(request, 'memoryBankApp/contact.html', {})

def testform(request):
	form = ListForm()
	context_dict = {'form': form}
	return render(request, 'memoryBankApp/testform.html', context_dict)

