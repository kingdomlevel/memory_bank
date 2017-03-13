from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from memoryBankApp.forms import ListForm, ListItemForm, EditItemForm
from memoryBankApp.models import List, ListItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

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

	newItemform = ListItemForm()
	if request.method == 'POST' and 'submitAdd' in request.POST:
		# pass the POST to form through forms.py
		newItemform = ListItemForm(request.POST)
		print "SUBMITTED!!!"
		if newItemform.is_valid():
			print newItemform.fields
			# pass the list ID from the POST to a variable
			id = request.POST.get('listID')
			print request.POST.get('listID')
			# save the form to a variable but don't commit to database
			newItem = newItemform.save(commit=False)
			# update the List attribute of list item
			newItem.list_id = id
			newItem.save()
			pass
		else:
			# print errors to the terminal
			print(newItemform.errors)

	editItemForm = EditItemForm()



	#instance = ListItem.objects.filter(user=request.user)
	if request.method == 'POST' and 'submitEdit' in request.POST:
		editItemForm = EditItemForm(request.POST)
		if editItemForm.is_valid():
			editItemForm.save()
		else:
			print(editItemForm.errors)

	allLists = List.objects.filter(user=request.user)
	allLists = allLists.order_by('-modified_date')
	listCount = len(allLists)		# gets total number of lists
	context_dict = {'allLists': allLists, 'listCount': listCount, 'form': newItemform, 'editItemForm':editItemForm}
	return render(request, 'memoryBankApp/home.html', context_dict)

def edit_item(request, id=None):
	instance = get_object_or_404(ListItem, id=id)
	editItemForm = EditItemForm(request.POST or None, instance=instance)
	if editItemForm.is_valid():
		instance = editItemForm.save(commit = False)
		instance.save()
		# return HttpResponse('memoryBankApp/home.html')
	context = {'form':editItemForm, 'title': instance.title, }

	return render(request,'memoryBankApp/edititem.html', context )


def testlist(request):
	allLists = List.objects.filter(user=request.user)
	allLists = allLists.order_by('-modified_date')
	listCount = len(allLists)		# gets total number of lists
	context_dict = {'allLists': allLists, 'listCount': listCount}
	return render(request, 'memoryBankApp/testlist.html', context_dict)


def about(request):
	print(request.method)
	return render(request, 'memoryBankApp/about.html', {})


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
