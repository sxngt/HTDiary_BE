from litestar import Litestar
from infrastructure.database.conn import db
from controller.todo_controller import TodoController

db.init_app(DB_URL="postgresql://ysh8614:8614@localhost/postgres")

app = Litestar([TodoController], on_shutdown=[db.shutdown])

