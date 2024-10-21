from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/create/', CreateTaskView.as_view(), name='create-task'),
    path('tasks/<int:pk>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('tasks/', AllTasksView.as_view(), name='all-tasks'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
    path('users/', UserListView.as_view(), name='user-list')
]