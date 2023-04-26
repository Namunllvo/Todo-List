from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from articles.models import Todo
from articles.serializers import TodoSerializer, TodoCreateSerializer, TodoListSerializer

# Create your views here.
class TodoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # TodoListSerializer
        todo = Todo.objects.all()
        serializer = TodoListSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        # TodoCreateSerializer
        print(request.user)
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):
    def get():
        # TodoSerializer?
        pass
    def put():
        # TodoSerializer
        # update
        pass
    def delete():
        # Todo
        # delete
        pass

class TodoListView_BoardView(APIView):
    # 이곳은 모든 트렐로처럼 유저가 등록한 할일목록 중 공개로 돌린 할일만 보이게 하는 view
    def get():
        # 로그인한 유저만 todolist들을 볼수있고
        # todo중에 공유? public todolist를 로그인한 유저들만 볼수 있게 공유하고
        # private으로 만든 리스트는 유저의 개인 view에서만볼수있게 구성하기
        pass
