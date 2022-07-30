from django.contrib import admin
from django.urls import include, path

from todos.views import TodoListView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("todos.urls")),
    path("", TodoListView.as_view()),
]
