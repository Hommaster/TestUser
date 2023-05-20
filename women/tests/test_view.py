from django.test import TestCase
from django.urls import reverse

from women.models import MyUser, Books


class UserView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 13
        for user_num in range(number_of_users):
            MyUser.objects.create(
                username='Christian %s' % user_num,
                surname='Surname %s' % user_num,
                email='email%s@mail.ru' % user_num
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/accounts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('list_of_user'))
        self.assertEqual(resp.status_code, 200)

    def test_detail_view_of_user_full_address(self):
        resp = self.client.get('/api/profile/13/')
        self.assertEqual(resp.status_code, 200)


class BooksView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Books.objects.create(
            id=1,
            name_book='One Piece',
            author_name='Oda',
            year_written='1996',
            comment='One Piece is REAL'
        )

    def test_books_list_view(self):
        resp = self.client.get('/api/books/list/')
        self.assertEqual(resp.status_code, 200)

    def test_books_list_view_name(self):
        resp = self.client.get(reverse('books_list'))
        self.assertEqual(resp.status_code, 200)

    def test_books_detail_view(self):
        resp = self.client.get('/api/books/detail/1/')
        self.assertEqual(resp.status_code, 200)
