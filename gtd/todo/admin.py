
from django.contrib import admin

from gtd.todo.models import TodoList
from gtd.todo.models import TodoItem

admin.site.register(TodoItem)
admin.site.register(TodoList)
