from database.models.customer import Customer
from database.repositories.base_repository import Repository
from utils.singleton import singleton


@singleton
class CustomerController:
    def __init__(self):
        self.customers = []
        
    # def add_customer(self, customer):
    #     pass

    def delete_customer(self, customer_id):
        repository = Repository[Customer]()
        session = repository.session
        try:
            # Retrieve the customer within the same session
            customer = session.query(Customer).filter(Customer.id == customer_id).first()
            if customer:
                repository.delete(customer)  # Call the delete method from the repository
            else:
                print(f"Customer with ID {customer_id} not found.")
        finally:
            session.close()  # Always close the session

    # def get_detail_customers(self):
    #     pass
    # def filter_customers(self, customers):
    #     pass

    def search_customers_by_last_name(self, lastname):
        repository = Repository[Customer]()
        session = repository.session
        customers = session.query(Customer).filter(Customer.lastname.ilike(f'%{lastname}%')).all()
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
        
