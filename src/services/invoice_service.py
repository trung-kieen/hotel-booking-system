"""
Author: Dang Xuan Lam
"""
from database.models.invoice import Invoice
from database.repositories.base_repository import Repository
from database.repositories.invoice_repository import InvoiceRepository


class InvoiceService:
    def __init__(self):
        self.invoice_repository = InvoiceRepository[Invoice]()

    def get_invoice_by_id(self, invoice_id):
        return self.invoice_repository.get([Invoice.id == invoice_id])

    def get_all_invoices(self):
        return self.invoice_repository.get_all()

    def filter_invoice(self, customer_phone, booking_status, pay_status, completed_date):
        return self.invoice_repository.filter(customer_phone, booking_status, pay_status, completed_date)
