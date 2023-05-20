
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import MyUser, Books
from .serializers import UserSerializer, UserDetailSerializer, BooksViewSerializer, BooksDetailSerializer


class UserRegister(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data)


class UserAPIView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]


class BooksApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksViewSerializer


class BooksDetailAPIView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializer
