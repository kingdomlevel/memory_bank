from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from memoryBankApp.forms import ListForm, ListItemForm
from memoryBankApp.models import List, ListItem
from django.contrib.auth.models import User


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

# def home(request):
# 	allLists = List.objects.all()
# 	allLists = List.objects.filter(List.user)
# 	context_dict = {'allLists': allLists,}
# 	return render(request, 'memoryBankApp/home.html', context_dict)

def home(request):
    allLists = List.objects.filter(user = request.user)
    allLists = allLists.order_by('-modified_date')
    listCount = len(allLists) #gets total number of lists
    context_dict = {'allLists': allLists, 'listCount':listCount}
    return render(request, 'memoryBankApp/home.html', context_dict)

def testlist(request):
	list1 = List.objects.get(title='list1')
	list2 = List.objects.get(title='list2')
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
	if request.method == 'POST':
		form = ListForm(request.POST)
		# check validity of form
		if form.is_valid():

			# save new list
			newList = form.save(commit=False)
			# update username to current user
			newList.user = request.user
			# post change to database
			newList.save()
			# return to user's home page
			return home(request)
		else:
			# print errors to the terminal
			print(form.errors)

	context_dict = {'form': form}
	return render(request, 'memoryBankApp/testform.html', context_dict)

def testitemform(request):
	form = ListItemForm()
	if request.method == 'POST':
		form = ListItemForm(request.POST)
		# check validity of form
		if form.is_valid():
			# save new list to database
			form.save(commit=True)
			# return to user's home page
			return home(request)
		else:
			# print errors to the terminal
			print(form.errors)

	context_dict = {'form': form}
	return render(request, 'memoryBankApp/testitemform.html', context_dict)