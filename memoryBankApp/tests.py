from django.test import TestCase


class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_memoryBankApp import populate
            populate()
        except ImportError:
            print('The module populate_memoryBankApp does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_list(self, title):
        from memoryBankApp.models import List

        try:
            list = List.objects.get(title=title)
        except List.DoesNotExist:
            list = None
        return list

    def get_list_item(self, title):
        from memoryBankApp.models import ListItem

        try:
            item = ListItem.objects.get(title=title)
        except ListItem.DoesNotExist:
            item = None
        return item

    def test_shopping_list_added(self):
        list = self.get_list('Shopping')
        self.assertIsNotNone(list)

    def test_list_created_today(self):
        from datetime import datetime

        list = self.get_list('Shopping')
        self.assertEquals(list.created_date.date(), datetime.today().date())

    def test_beans_list_item_added(self):
        item = self.get_list_item('Beans')
        self.assertIsNotNone(item)

    # Test whether previously validated item is in list 'Shopping'
    def test_beans_list_item_in_shopping_list(self):
        # The list's id is the item's foreign key
        item = self.get_list_item('Beans')
        item_list_id = item.list.id

        # Get 'Shopping' list's id
        list = self.get_list('Shopping')
        list_id = list.id

        self.assertEquals(list_id, item_list_id, 'Beans is not in Shopping list')

    def test_list_belongs_to_mike(self):
        from django.contrib.auth.models import User
        from memoryBankApp.models import List

        user_mike = User.objects.get(username='mike')
        user_list = List.objects.get(title='Shopping').user
        self.assertEqual(user_mike, user_list)


class ViewTestsNoLists(TestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        try:
            user = User.objects.create_user(
                username='mike',
                password='P@ssword',
                email='mike@mike.com',
                first_name='mike',
                last_name='teller'
            )
            user.save()
        except:
            print('Something went wrong in the creation of mike :(')

    def test_call_home_view_denies_anonymous(self):
        # Not logged in should redirect to login
        response = self.client.get('/memorybank/home/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/memorybank/home/')
        response = self.client.post('/memorybank/home/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/memorybank/home/')

    def test_call_home_view_loads_for_user(self):
        # login as 'mike'
        login = self.client.login(username='mike', password='P@ssword')
        self.assertTrue(login)

        # Access home, expect status 200 OK HttpResponse
        response = self.client.get('/memorybank/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memoryBankApp/home.html')

    def test_home_displays_no_lists_message(self):
        # Check if no lists message is displayed
        login = self.client.login(username='mike', password='P@ssword')
        response = self.client.get('/memorybank/home/')
        self.assertIn("You don't have any lists yet", response.content)


class ViewTestsWithLists(TestCase):

    def setUp(self):
        try:
            from populate_memoryBankApp import populate
            populate()
        except ImportError:
            print('The module populate_memoryBankApp does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def test_quick_item_form_is_correct(self):
        from memoryBankApp.forms import QuickItemForm

        login = self.client.login(username='mike', password='P@ssword')
        response = self.client.get('/memorybank/home/')
        self.assertIsNotNone(response.context)

        form = response.context['quick_item_form']
        self.assertTrue(isinstance(form, QuickItemForm))
        self.assertInHTML('<input class="form-quick-item" id="id_title" name="title" placeholder="Quick item..." type="text" required />', response.content)

    def test_update_list_context_returns_correct_list(self):
        from memoryBankApp.models import List

        login = self.client.login(username='mike', password='P@ssword')

        # Post id of the 'Shopping' list and get list from the returned context
        list_id = List.objects.get(title='Shopping').id
        response = self.client.post('/memorybank/update_list/', {'list_id' : list_id})
        list = response.context['List']

        self.assertEqual(list.title, 'Shopping')

    def test_quick_item_view_creates_milk_adds_to_shopping(self):
        from memoryBankApp.models import ListItem
        from memoryBankApp.models import List

        login = self.client.login(username='mike', password='P@ssword')

        item_milk = 'Milk'
        shopping_list = List.objects.get(title='Shopping')
        # Simulate form action and create new item 'Milk' in 'Shopping'
        response = self.client.post('/memorybank/quick_item/', {'title' : item_milk, 'list_id' : shopping_list.id})

        # Check whether the item now appears in the 'Shopping' list's listitem_set
        list = response.context['List']
        self.assertEqual(list, shopping_list)
        self.assertTrue(list.listitem_set.filter(title=item_milk).exists())
