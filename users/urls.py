from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views


urlpatterns = [
    path('', views.UserDetailView.as_view(), name='user-detail-view'),
    path('signup/', views.UserView.as_view(), name='user-signup-view'),
    path('mock/', views.mockView.as_view(), name='mock-view'),
     # payload 커스텀
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]