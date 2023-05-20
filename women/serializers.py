from rest_framework import serializers

from .models import MyUser, Books


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = MyUser(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: 'Пароль не совпадает'})
        user.set_password(password)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'surname', 'email']


class BooksViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BooksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
