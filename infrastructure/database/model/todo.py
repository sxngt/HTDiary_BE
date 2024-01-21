from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table, Date

engine = create_engine("postgresql://ysh8614:8614@localhost/postgres")
metadata = MetaData()

todo_table = Table("todos", metadata,
                   Column("id", Integer, primary_key=True),
                   Column("title", String),
                   Column("description", String),
                   Column("date", Date)
                   )

metadata.create_all(engine)

#TODO 중복 테이블 존재 시에 작동을 안하는데, 해당 로직 개선해서 덮어쓰기도 가능하도록 해봐야 함