"""
Author: Hoang Le Thuy Hoa
"""
from database.models.customer import Customer
from database.repositories.base_repository import Repository
from utils.singleton import singleton
from utils.logging import app_logger

from sqlalchemy import or_


@singleton
class CustomerController:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        return Repository[Customer]().insert(customer)

    def delete_customer(self, customer_id):
        repository = Repository[Customer]()
        session = repository.session
        try:
            # Retrieve the customer within the same session
            customer = session.query(Customer).filter(Customer.id == customer_id).first()
            if customer:
                repository.delete(customer)  # Call the delete method from the repository
            else:
                app_logger.info(f"Customer with ID {customer_id} not found.")
        finally:
            session.close()  # Always close the session

    def search_customers_by_firstname_or_lastname(self, name):
        repository = Repository[Customer]()
        session = repository.session
        customers = session.query(Customer).filter(
            or_(
                Customer.firstname.ilike(f'%{name}%'),
                Customer.lastname.ilike(f'%{name}%')
            )
        ).all()

        return customers

    def update_customer(self, customer):
        return Repository[Customer]().update(customer)

    def find_customer_by_id(self, customer_id):
        repository = Repository[Customer]()
        session = repository.session
        try:
            # Retrieve the customer within the same session
            customer = session.query(Customer).filter(Customer.id == customer_id).first()
            return customer
        finally:
            session.close()  # Always close the session

    def get_all_customers(self):
        return Repository[Customer]().get_all()
