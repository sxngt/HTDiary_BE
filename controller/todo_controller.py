from litestar import Controller, get
from datetime import *


class TodoController(Controller):
    path = "/todo"

    @get(path="/all")
    def getAllTodo(self) -> str:
        return ""

    @get(path="/")
    def getTodoByDay(self, date: str) -> str:
        return ""




