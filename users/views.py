from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer, UserDetailSerializer, CustomTokenObtainPairSerializer
from users.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)


# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        

class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]      # 로그인 할때만 볼수 있다
    def get(self, request):
        # 로그인 한 유저의 회원가입 정보
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        # 저장된 회원 정보 수정
        user = User.objects.get(id=request.user.id)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정완료!"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # 저장된 회원 삭제하기
        # permission_classes = [permissions.IsAuthenticated]
        user = User.objects.get(id=request.user.id)
        if user:
            user.delete()
            return Response({"message":"회원탈퇴!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"!!!!에러에러에러!!!"}, status=status.HTTP_400_BAD_REQUEST)


# payload 커스텀
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# 로그인이 된 상태인지 확인하는 뷰
class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        user = request.user
        # user.is_admin = True
        user.save()
        return Response(f"{request.user.username}님이 로그인하셨습니다")
    


# # 로그아웃
# class UserLogoutView(APIView):
#     permission_classes = [permission_classes.IsAuthenticated]
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)