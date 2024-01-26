from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql://ysh8614:8614@localhost/postgres")
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    date = Column(Date)


Base.metadata.create_all(engine)

# TODO 중복 테이블 존재 시에 작동을 안하는데, 해당 로직 개선해서 덮어쓰기도 가능하도록 해봐야 함
