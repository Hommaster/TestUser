from django.test import TestCase

from django.urls import reverse
from rest_framework import status


class UserTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.data = {
            'username': 'user',
            'email': 'mail@mail.ru',
            'password': '31012002sesiD',
            'password2': '31012002sesiD',
        }

    def test_create_user(self):
        response = self.client.post(self.register_url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)