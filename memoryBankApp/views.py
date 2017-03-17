from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from memoryBankApp.forms import ListForm, ListItemForm, EditItemForm, EnhancedListForm
from memoryBankApp.models import List, ListItem, BankItem, EnhancedList
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



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

@login_required
def home(request):
	newItemform = ListItemForm()
	newListForm = ListForm()
	if request.method == 'POST' and 'submitAdd' in request.POST:
		# pass the POST to form through forms.py
		newItemform = ListItemForm(request.POST)
		print "SUBMITTED!!!"
		if newItemform.is_valid():
			print newItemform.fields
			# pass the list ID from the POST to a variable
			id = request.POST.get('listID')
			# save the form to a variable but don't commit to database
			newItem = newItemform.save(commit=False)

			# update the List attribute of list item
			newItem.list_id = id
			newItem.save()
			newItemform = ListItemForm()

			#Add the title of the list item to the bank (BankItems model)
			bankTitle = request.POST.get('title')
			bankItem = BankItem.objects.create(title = bankTitle)
			bankItem.save()
			print (bankItem.title)
			return HttpResponseRedirect('/memorybank/home')
			pass
		else:
			# print errors to the terminal
			print(newItemform.errors)
	if request.method == 'POST' and 'submitAddList' in request.POST:
		newListForm = ListForm(request.POST)
		print("NEW LIST ADDED")
		if newListForm.is_valid():
			# save new list
			newList = newListForm.save(commit=False)
			# update username to current user
			newList.user = request.user
			# post change to database
			newList.save()
			# return to user's home page
			newListForm = ListForm()
			return HttpResponseRedirect('/memorybank/home')
		else:
			# print errors to the terminal
			print(newListForm.errors)


	editItemForm = EditItemForm()


	#NOT CURRENTLY USED
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
	allListsCol1 = allLists[0::3]
	allListsCol2 = allLists[1::3]
	allListsCol3 = allLists[2::3]
	context_dict = {'allLists': allLists, 'allListsCol1': allListsCol1,
					'allListsCol2': allListsCol2, 'allListsCol3': allListsCol3,
					'listCount': listCount, 'form': newItemform,
					'editItemForm':editItemForm, 'ListForm': newListForm}
	return render(request, 'memoryBankApp/home.html', context_dict)

@login_required
def edit_item(request, id=None):
	instance = get_object_or_404(ListItem, id=id)
	parentList = instance.list
	parentUser = parentList.user
	if (parentUser != request.user):
		return HttpResponse("You are not authorised to access this content")
	else:
		#if request.method == 'POST' and 'submitSave' in request.POST:
		editItemForm = EditItemForm(request.POST or None, instance=instance)
		if editItemForm.is_valid():
			remove = request.POST.get('removeFormField')
			instance = editItemForm.save(commit = False)
			instance.removed = remove
			instance.save()
			# redirect to home after saving changes or removing item from list
			editItemForm = EditItemForm() #check this
			return HttpResponseRedirect('/memorybank/home')
	context = {'form':editItemForm, 'title': instance, }
	return render(request,'memoryBankApp/edititem.html', context )


def bank_display(request):
	bank_list = []
	starts_with = ''
	if request.method =='GET':
		starts_with= request.GET['suggestion']
		bank_list = bankItems(100, starts_with)
		print(bank_list)

	return render(request, 'memoryBankApp/banklist.html', {'bank_list': bank_list})

def bankItems(max_results=0, starts_with=''):
	bank_list = []
	if starts_with:
		bank_list = BankItem.objects.filter(name__istartswith=starts_with)
		print(bank_list)
		print(starts_with)
	if max_results>0:
		if len(bank_list)>max_results:
			bank_list = bank_list[:max_results]
		return bank_list

def banktest(request):
	banklist = BankItem.objects.filter()[:100]
	context = {'banklist': banklist}
	return render(request,  'memoryBankApp/banktest.html', context)

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
	return render(request, 'memoryBankApp/testitem.html', context_dict)


def enhancedlist(request):
	form = EnhancedListForm()
	if request.method == 'POST':
		form = EnhancedListForm(request.POST)
		if form.is_valid():
			print("POSTED")
			text = request.POST.get('editor1')
			new_enhanced = form.save(commit=False)
			new_enhanced.long_text = text
			new_enhanced.save()
			form = EnhancedListForm()
			return HttpResponseRedirect('/memorybank/home')
		else:
			print("NOT POSTED!!!!!")
			print(form.errors)

	context_dict = {'form': form}
	return render(request, 'memoryBankApp/enhancedlist.html', context_dict)
