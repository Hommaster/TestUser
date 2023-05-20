from django.test import TestCase

from women.models import MyUser, Books


class TestModelUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        Books.objects.create(
            name_book='One Piece',
            author_name='Oda',
            year_written='1996',
            comment='One Piece is REAL'
        )
        booker = Books.objects.get(id=1)
        MyUser.objects.create(
            username='user',
            surname='surname',
            email='mail@mail.ru',
            books=booker
        )

    def test_user_model(self):
        users = MyUser.objects.get(id=1)
        field_label = users._meta.get_field('books').verbose_name
        self.assertEqual(field_label, 'books')


class BooksTest(TestCase):
    def setUp(self):
        self.book = Books.objects.create(
            name_book='One Piece',
            author_name='Oda',
            year_written='1996',
            comment='One Piece is REAL'
        )

    def test_model_book(self):
        self.name_book = self.book.name_book
        self.author_name = self.book.author_name
        self.year_written = self.book.year_written
        self.comment = self.book.comment
        self.assertEqual(self.name_book, 'One Piece')
        self.assertEqual(self.author_name, 'Oda')
        self.assertEqual(self.year_written, '1996')
        self.assertEqual(self.comment, 'One Piece is REAL')
