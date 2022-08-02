from django.contrib.auth import get_user_model
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Todo
from .serializers import TodoSerializer, UserSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_class = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
