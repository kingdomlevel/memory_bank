from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from memoryBankApp.forms import ListForm, ListItemForm, EditItemForm, EnhancedListForm, DeleteListForm
from memoryBankApp.models import List, ListItem, BankItem, EnhancedList
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



def index(request):

	response = render(request, 'memoryBankApp/index.html')
	return response



@login_required
def home(request, id=None):
	newItemform = ListItemForm()
	newListForm = ListForm()
	del_list_form = DeleteListForm()
	if request.method == 'POST' and 'submitAdd' in request.POST:
		# pass the POST to form through forms.py
		newItemform = ListItemForm(request.POST)
		if newItemform.is_valid():
			print newItemform.fields
			# pass the list ID from the POST to a variable
			title = request.POST.get("banktitle")
			id = request.POST.get('listID')
			# save the form to a variable but don't commit to database
			newItem = newItemform.save(commit=False)

			#update list item title
			newItem.title = title
			# update the List attribute of list item
			newItem.list_id = id
			newItem.save()
			newItemform = ListItemForm()

			#Add the title of the list item to the bank (BankItems model)
			bankTitle = title
			bankItem = BankItem.objects.create(title = bankTitle)
			bankItem.user = request.user
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

	if request.method == 'POST' and 'submitDeleteList' in request.POST:
		l_id = request.POST.get('listID')
		remove = request.POST.get('listDeleteBool')
		List.objects.filter(id=l_id).update(removed=remove)
		return HttpResponseRedirect('/memorybank/home')


	bankTitleList = getSetOfBankTitles(request)

	allLists = List.objects.filter(user=request.user, removed='0')
	allLists = allLists.order_by('-modified_date')
	listCount = len(allLists)		# gets total number of lists

	allEnhanced = EnhancedList.objects.filter(user=request.user)
	allEnhanced = allEnhanced.order_by('title')

	allListsCol = []
	cols = 3
	for i in range(cols):
		allListsCol.append(allLists[i::cols])

	context_dict = {'allLists': allLists, 'allListsCol': allListsCol,
					'listCount': listCount, 'form': newItemform,
					'ListForm': newListForm, 'banklist': bankTitleList,
					'allEnhanced': allEnhanced, 'enhancedCount': allEnhanced}

	return render(request, 'memoryBankApp/home.html', context_dict)





def getSetOfBankTitles(request):
	banklist = BankItem.objects.filter()[:100]
	bankTitleList = set()
	for b in banklist:
		if b.user_id==request.user.id:
			bankTitleList.add(b.title)
	return bankTitleList





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


@login_required
def edit_enhanced_list(request, id=None):
	instance = get_object_or_404(EnhancedList, id=id)
	user = instance.user_id
	if (user != request.user.id):
		return HttpResponse("You are not authorised to access this content")
	else:
		enhanced_list_form = EnhancedListForm(request.POST or None, instance=instance)
		if enhanced_list_form.is_valid():
			instance = enhanced_list_form.save(commit=False)
			text = request.POST.get('editor1')
			instance.long_text = text
			instance.save()
			return HttpResponseRedirect('/memorybank/home')
	context={'form': enhanced_list_form,}

	return render(request,'memoryBankApp/editenhancedlist.html', context )


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

@login_required
def enhancedlist(request):
	form = EnhancedListForm()
	if request.method == 'POST':
		form = EnhancedListForm(request.POST)
		if form.is_valid():
			text = request.POST.get('editor1')
			user = request.user
			new_enhanced = form.save(commit=False)
			new_enhanced.long_text = text
			new_enhanced.user = user
			new_enhanced.save()
			form = EnhancedListForm()
			return HttpResponseRedirect('/memorybank/home')
		else:
			print(form.errors)
	allEnhanced = EnhancedList.objects.filter(user=request.user)
	allEnhanced = allEnhanced.order_by('title')
	context_dict = {'form': form, 'allEnhanced': allEnhanced,}
	return render(request, 'memoryBankApp/enhancedlist.html', context_dict)
