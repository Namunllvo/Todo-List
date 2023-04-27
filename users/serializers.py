from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from articles.serializers import TodoListSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        # print(validated_data)
        password = user.password
        # print(user.password)
        user.set_password(password)     # pw hashing 암호화
        # print(user.password)
        user.save()
        return user

    # instance : 수정할 object
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    todo_set = TodoListSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__" # 원래 있던필드 + 추가한 필드



    # payload 커스텀 - user_id(기본)에 email추가
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['gender'] = user.gender
        token['age'] = user.age

        return token