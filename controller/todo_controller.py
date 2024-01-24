from litestar import Controller, get
from application.todo_service import TodoService
from litestar.di import Provide


class TodoController(Controller):
    path = "/todo"
    dependencies = {"todoService": Provide(TodoService)}

    @get(path="/all")
    def get_all_todo(self, todoService: TodoService) -> str:
        return todoService.get_all_todo()

    @get(path="/")
    def getTodoByDay(self, date: str) -> str:
        return ""




