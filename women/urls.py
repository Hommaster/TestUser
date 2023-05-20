from django.urls import path

from .views import UserRegister, UserAPIView, UserDetailAPIView, BooksApiView, BooksDetailAPIView

urlpatterns = [
    path('books/list/', BooksApiView.as_view(), name='books_list'),
    path('books/detail/<int:pk>/', BooksDetailAPIView.as_view()),
    path('register/', UserRegister.as_view(), name='register'),
    path('accounts/', UserAPIView.as_view(), name='list_of_user'),
    path('profile/<int:pk>/', UserDetailAPIView.as_view(), name='detail-profile'),
]
