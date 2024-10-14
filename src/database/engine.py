from sqlalchemy import create_engine

from utils.settings import DATABASE_SQLITE_FILE
from utils.singleton import singleton
@singleton
class EngineHolder:
    def __init__(self) -> None:
        self.engine = create_engine(f"sqlite:///{DATABASE_SQLITE_FILE}", echo=True)

    def get_engine(self):
        return self.engine
