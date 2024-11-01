"""
Author: Dang Xuan Lam
"""
import abc
from abc import abstractmethod
from typing import TypeVar, Generic, Iterable, Any

from database.engine import EngineHolder
from sqlalchemy.orm import create_session, Bundle, Session, sessionmaker, scoped_session

from database.orm import Base

T = TypeVar('T', bound=Base)


@abc.abstractmethod
class IRepository(abc.ABC, Generic[T]):

    def __init__(self):
        self.engine = EngineHolder().get_engine()
        self.session = scoped_session(sessionmaker(bind=self.engine))()

    @abstractmethod
    def insert(self, item: T) -> None:
        pass

    @abstractmethod
    def delete(self, item: T) -> None:
        pass

    @abstractmethod
    def update(self, item: T) -> None:
        pass

    @abstractmethod
    def get(self, _filter: list[Any]) -> T:
        pass

    @abstractmethod
    def insert_all(self, items: Iterable[T]) -> None:
        pass

    @abstractmethod
    def update_all(self, items: Iterable[T]) -> None:
        pass

    @abstractmethod
    def get_all(self, _filter: list[Any]) -> Iterable[T]:
        pass
