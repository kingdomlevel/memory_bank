# memory_bank

Shared repository for our team *The Wranglers*, and our group project **memoryBank**.


### Niall's Django Cheat Sheet
I took most of the "summary" sections at the end of each chapter in the *Tango with Django* book and made the following cheat sheet 🌴

##### Creating a new Django Project
1.	To create the project run, python django-admin.py startproject <name>, where <name> is the name of the project you wish to create.

#### Creating a new Django application
1.	To create a new application, run `$ python manage.py startapp <appname>`, where <appname> is the name of the application you wish to create.
2.	Tell your Django project about the new application by adding it to the INSTALLED_APPS tuple in your project’s settings.py file.
3.	In your project urls.py file, add a mapping to the application.
4.	In your application’s directory, create a urls.py file to direct incoming URL strings to views.
5.	In your application’s view.py, create the required views ensuring that they return a HttpResponse object.

#### Creating and integrating a Django template
1.	First, create the template you wish to use and save it within the templates directory you specified in your project’s settings.py module. You may wish to use Django template variables (e.g. `{{ variable_name }}`) or template tags within your template. You’ll be able to replace these with whatever you like within the corresponding view.
2.	Find or create a new view within an application’s views.py file.
3.	Add your view specific logic (if you have any) to the view. For example, this may involve extracting data from a database and storing it within a list.
4.	Within the view, construct a dictionary object which you can pass to the template engine as part of the template’s context.
5.	Make use of the `render()` helper function to generate the rendered response. Ensure you reference the request, then the template file, followed by the context dictionary.
6.	If you haven’t already done so, map the view to a URL by modifying your project’s urls.py file and the application specific urls.py file if you have one.

#### Get static media onto one of your pages
1.	Take the static media file you wish to use and place it within your project’s static directory. This is the directory you specify in your project’s STATICFILES_DIRS list within settings.py.
2.	Add a reference to the static media file to a template. For example, an image would be inserted into an HTML page through the use of the `<img />` tag.
3.	Remember to use the `{% load staticfiles %}` and `{% static "<filename>" %}` commands within the template to access the static files. Replace <filename> with the path to the image or resource you wish to reference. Whenever you wish to refer to a static file, use the static template tag!

#### Serve some media my friend
1.	Place a file within your project’s media directory. The media directory is specified by your project’s MEDIA_ROOT variable.
2.	Link to the media file in a template through the use of the `{{ MEDIA_URL }}` context variable. For example, referencing an uploaded image cat.jpg would have an `<img />` tag like `<img src="{{ MEDIA_URL}}cat.jpg">`.


#### Model Setup
Now that we’ve covered the core principles of dealing with Django’s ORM, now is a good time to summarise the processes involved in setting everything up. We’ve split the core tasks into separate sections for you. Check this section out when you need to quickly refresh your mind of the different steps.
Setting up your Database
With a new Django project, you should first tell Django about the database you intend to use (i.e. configure DATABASES in settings.py). You can also register any models in the admin.py module of your app to make them accessible via the admin interface.
Adding a Model
The workflow for adding models can be broken down into five steps.

1.	First, create your new model(s) in your Django application’s models.py file.

2.	Update admin.py to include and register your new model(s).

3.	Perform the migration `$ python manage.py makemigrations <app_name>`.

4.	Apply the changes `$ python manage.py migrate`. This will create the necessary infrastructure within the database for your new model(s).

5.	Create/edit your population script for your new model(s).

##### Invariably, there will be times when you will have to delete your database. When this happens, run the following commands from the manage.py module.
1.	migrate your database - this will set everything up in the new database. Ensure that your app is listed in the migrations that are committed. If it is not, run the makemigrations <app_name> command, where <app_name> is the name of your app.
2.	Create a new administrative account with the createsuperuser command.

#### Cleaning Form Data

⁃	Form data is obtained from the ModelForm dictionary attribute cleaned_data.

⁃	Form fields that you wish to check can then be taken from the cleaned_data dictionary. Use the .get() method provided by the dictionary object to obtain the form’s values. If a user does not enter a value into a form field, its entry will not exist in the cleaned_data dictionary. In this instance, .get() would return None rather than raise a KeyError exception. This helps your code look that little bit cleaner!

⁃	For each form field that you wish to process, check that a value was retrieved. If something was entered, check what the value was. If it isn’t what you expect, you can then add some logic to fix this issue before reassigning the value in the cleaned_data dictionary.
⁃	You must always end the clean() method by returning the reference to the cleaned_data dictionary. Otherwise the changes won't be applied
