from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


class SQLAlchemy:
    def __init__(self):
        self._engine = None
        self._session = None

    def init_app(self, **kwargs):
        """
        DB 초기화 함수
        :param kwargs: DB_URL, DB_POOL_RECYCLE, DB_ECHO 등등
        """
        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)

        self._engine = create_engine(
            database_url,
            echo=echo,
            pool_recycle=pool_recycle,
            pool_pre_ping=True,
        )

        self._session = sessionmaker(bind=self._engine, autoflush=False)

        self._engine.connect()
        print("DB connected")

    def shutdown(self):
        self._session.close_all()
        self._engine.dispose()
        print("DB disconnected")

    def get_db(self):
        """
        요청마다 DB 세션 유지
        """
        if self._session is None:
            raise Exception("Must be called 'init_app'")
        db_session = None
        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db()

    @property
    def engine(self):
        return self._engine


db = SQLAlchemy()
Base = declarative_base()
