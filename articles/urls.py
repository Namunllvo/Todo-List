from django.urls import path
from articles import views

urlpatterns = [
    path('', views.TodoView.as_view(), name='todo_view'),
    path('<int:todo_id>/', views.TodoDetailView.as_view(), name='todo_detail_view'),
    path('board/', views.TodoListView_BoardView.as_view(), name='board_view'),
]
