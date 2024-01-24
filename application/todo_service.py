from application.repository.todo_repository import TodoRepository
from application.entity.todo import Todo
from infrastructure.database.conn import db


class TodoService:
    todo_repository = TodoRepository(db.session, Todo)

    def get_all_todo(self):
        return self.todo_repository.get_all_todo()
