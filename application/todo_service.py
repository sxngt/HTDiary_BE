from domain.repository.todo_repository import TodoRepository
from infrastructure.database.model.todo import Todo
from infrastructure.database.conn import db


class TodoService:
    todo_repository = TodoRepository(next(db.session), Todo)

    def get_all_todo(self):
        print(db.session.query(Todo).all())
        return self.todo_repository.get_all_todo()
