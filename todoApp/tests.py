from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import TodoItem

class TodoApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.userJohn = User.objects.create_user(
            username='john', password='top_secret')
        self.userJane = User.objects.create_user(
            username='jane', password='top_secret')
        TodoItem.objects.create(added_by=self.userJohn, title='todo-john')
        TodoItem.objects.create(added_by=self.userJane, title='janes-todo-1')
        TodoItem.objects.create(added_by=self.userJane, title='janes-todo-2')

    def test_get_todos_anon(self):
        """
        test that anonymous users can't view todos
        """
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_todos_authenticated(self):
        """
        test that an authenticated user sees her/his own todos
        """
        self.client.login(username='john', password='top_secret')
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = response.data['results']
        self.assertEqual(len(res_data), 1)
        self.assertEqual(res_data[0]['added_by'], 'john')
        self.assertEqual(res_data[0]['is_done'], False)

    def test_anon_user_cant_create_todos(self):
        """
        test that an anonymous user can't create a todo item
        """
        response = self.client.post('/todos/', {"title": "john's second todo"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_todos(self):
        """
        test that an authenticated user can create a todo item
        """
        self.client.login(username='john', password='top_secret')
        response = self.client.post('/todos/', {"title": "john's second todo"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


