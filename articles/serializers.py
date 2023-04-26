from rest_framework import serializers
from articles.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()      # 커스텀 필드 밑의 def get_user를 return 값으로 돌아감

    def get_user(self, obj):    # 위의 user와 이름이 다르면 에러가 나요!!!!
        return obj.user.username

    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "content")

class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Todo
        fields = ("pk", "username", "title", "comment", "is_complete", "completion_at")