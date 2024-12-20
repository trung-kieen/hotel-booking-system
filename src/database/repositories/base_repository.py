"""
Author: Dang Xuan Lam
"""
from typing import Iterable, Any

from utils.logging import app_logger

from sqlalchemy import and_

from database.repositories.irepository import IRepository, T
from utils.singleton import singleton


class Repository(IRepository[T]):

    def __init__(self):
        super().__init__()

    def insert(self, item: T) -> None:
        self.session.add(item)
        self.session.commit()
        # self.session.close()

    def delete(self, item: T) -> None:
        self.session.delete(item)
        self.session.commit()

    def update(self, item: T) -> None:
        keys = [k.name for k in self.__orig_class__.__args__[0].__mapper__.primary_key]
        primary_key_values = {key: getattr(item, key) for key in keys}
        existing_item = self.session.query(type(item)).filter_by(**primary_key_values).first()

        if existing_item:
            # Merge the incoming item into the session to avoid session conflicts
            merged_item = self.session.merge(item)
            self.session.commit()
        else:
            app_logger.info(f"Item with primary key {primary_key_values} not found.")


    def get(self, _filters: list[Any] = []) -> T:
        """ get object of type T base on filter (optional)
         Example: Repository()[Customer].get(filter = [Customer.name = "didy"])
         """
        query = self.session.query(self.__orig_class__.__args__[0])

        if _filters:
            if len(_filters) == 1:
                query = query.filter(_filters[0])  # Nếu chỉ có một điều kiện
            else:
                query = query.filter(and_(*_filters))  # Nếu có nhiều điều kiện

        return query.first()

    def insert_all(self, items: Iterable[T]) -> None:
        self.session.add_all(items)
        self.session.commit()

    def update_all(self, items: Iterable[T]) -> None:
        for item in items:
            self.update(item)

    def get_all(self, _filters: list[Any] = []) -> Iterable[T]:
        """ get list object of type T base on filter (optional)
            Example: Repository()[Customer].get(filter = [Customer.name = "didy"])
         """
        query = self.session.query(self.__orig_class__.__args__[0])

        if _filters:
            if len(_filters) == 1:
                query = query.filter(_filters[0])
            else:
                query = query.filter(and_(*_filters))

        return query.all()
