
from django.contrib import admin

from gtd.todo.models import TodoList
from gtd.todo.models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    model = TodoItem
    filter_horizontal = ('todo_lists',)

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(TodoList)
