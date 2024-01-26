from sqlalchemy.orm import Session


class TodoRepository:
    entity: object
    db: Session

    def __init__(self, db: Session, entity: object):
        self.db = db
        self.entity = entity

    def get_all_todo(self):
        res = self.db.query(self.entity).all()
        print(res)
        return res

