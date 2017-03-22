from django.shortcuts import render
from memoryBankApp.forms import ListForm, ListItemForm, EditItemForm, EnhancedListForm, DeleteListForm, QuickItemForm
from memoryBankApp.models import List, ListItem, BankItem, EnhancedList
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime


#Index Page
def index(request):
	response = render(request, 'memoryBankApp/index.html')
	return response


#Main Page containing all users lists.
@login_required
def home(request, id=None):
	#FORMS
	newItemform = ListItemForm()
	newListForm = ListForm()
	del_list_form = DeleteListForm()
	quick_item_form = QuickItemForm()

	#ADD LIST-ITEM function
	if request.method == 'POST' and 'submitAdd' in request.POST:
		add_item(newItemform,request) #see helper function below

	#ADD NEW LIST function
	if request.method == 'POST' and 'submitAddList' in request.POST:
		add_new_list(newListForm, request) #see helper function below

	#DELETE LIST function
	if request.method == 'POST' and 'submitDeleteList' in request.POST:
		l_id = request.POST.get('listID')
		remove = request.POST.get('listDeleteBool')
		List.objects.filter(id=l_id).update(removed=remove)
		return HttpResponseRedirect('/memorybank/home')

	#helper function get's a set of unique bank titles
	bankTitleList = getSetOfBankTitles(request)

	#gets all of users lists
	allLists = List.objects.filter(user=request.user, removed='0')
	allLists = allLists.order_by('-modified_date')
	listCount = len(allLists)		# gets total number of lists

	#Creates a matrix of all the lists for displaying in the template
	allListsCol = []
	cols = 3
	for i in range(cols):
		allListsCol.append(allLists[i::cols])

	context_dict = {'allLists': allLists, 'allListsCol': allListsCol,
					'listCount': listCount, 'form': newItemform,
					'ListForm': newListForm, 'quick_item_form': quick_item_form,
					'banklist': bankTitleList, }

	return render(request, 'memoryBankApp/home.html', context_dict)

#helper function for adding a new list
def add_new_list(newListForm, request):
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
		return

#helper function for adding new item
def add_item(newItemform,request):
	newItemform = ListItemForm(request.POST)
	if newItemform.is_valid():
		print newItemform.fields

		# pass the list ID and title from the POST to a variable
		title = request.POST.get("banktitle")
		id = request.POST.get('listID')

		# save the form to a variable but don't commit to database
		newItem = newItemform.save(commit=False)

		# update list item title
		newItem.title = title
		# update the List attribute of list item
		newItem.list_id = id
		newItem.save()
		newItemform = ListItemForm() #clears the form fields

		# Add the title of the list item to the bank (BankItems model)
		bankTitle = title
		bankItem = BankItem.objects.create(title=bankTitle)
		bankItem.user = request.user
		bankItem.save()
		print (bankItem.title)
		return HttpResponseRedirect('/memorybank/home')
		pass
	else:
		# print errors to the terminal
		print(newItemform.errors)
	return


#AJAX powered function to allow instant addition of list item
@login_required
def quick_item(request):
	quick_item_form = QuickItemForm()
	if request.method == 'POST':
		try:
			title = request.POST.get('title', '')
			list_id = request.POST.get('list_id', '')
			list = List.objects.get(pk=list_id)
			# new list item with default values except title
			newItem = ListItem(list=list, title=title, date=datetime.now(), priority='low', notes='', created_date=datetime.now(), modified_date=datetime.now())
			newItem.save()
		except Exception as e:
	    		print '%s (%s)' % (e.message, type(e))
	return render(request, 'memoryBankApp/update_list.html', {'List' : list})


@login_required
def update_list(request):
	quick_item_form = QuickItemForm()
	if request.method == 'POST':
		try:
			list_id = request.POST.get('list_id', '')
			list = List.objects.get(pk=list_id)
		except Exception as e:
	    		print '%s (%s)' % (e.message, type(e))
	return render(request, 'memoryBankApp/update_list.html', {'List' : list, 'quick_item_form' : quick_item_form})


#helper function to return a set of unique bank items belonging to the user
def getSetOfBankTitles(request):
	banklist = BankItem.objects.filter()[:200]
	bankTitleList = set()
	for b in banklist:
		if b.user_id==request.user.id:
			bankTitleList.add(b.title)
	return bankTitleList

#View allows user to edit a list item
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

#View allows user to edit the enhanced list
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


def about(request):
	print(request.method)
	return render(request, 'memoryBankApp/about.html', {})


def faq(request):
	print(request.method)
	return render(request, 'memoryBankApp/faq.html', {})


def contact(request):
	print(request.method)
	return render(request, 'memoryBankApp/contact.html', {})


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
