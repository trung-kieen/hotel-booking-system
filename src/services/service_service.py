"""
Author: Dang Xuan Lam
"""
from typing import List, Iterable

from database.models.service import Service
from database.repositories.base_repository import Repository
from utils.singleton import singleton


@singleton
class ServiceService:
    def __init__(self):
        self.service_repository = Repository[Service]()

    def get_service(self, service_id: int) -> Service:
        return self.service_repository.get([Service.id == service_id])

    def get_services(self) -> Iterable[Service]:
        return self.service_repository.get_all()

    def create_service(self, service: Service) -> None:
        self.service_repository.insert(service)

    def update_service(self, service: Service) -> None:
        self.service_repository.update(service)

    def delete_service(self, service_id: int):
        return self.service_repository.delete(self.service_repository.get([Service.id == service_id]))

    def search_services(self, keyword: str) -> List[Service]:
        return list(self.service_repository.get_all([Service.name.like(f"%{keyword}%")]))
