from django.urls import path
from todos.views import TodoListView

from .views import AboutPageView, HomePageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("todos/", TodoListView.as_view(), name="todolist"),
]
