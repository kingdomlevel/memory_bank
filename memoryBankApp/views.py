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
	print(request.method)
	#print(request.user)
	#response = render(request, 'memoryBankApp/home.html')
	return render(request, 'memoryBankApp/home.html',{})


def testlist(request):
	return render(request, 'memoryBankApp/testlist.html')


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

