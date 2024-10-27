from database.models.invoice import Invoice
from database.repositories.base_repository import Repository


class InvoiceService:
    def __init__(self):
        self.invoice_repository = Repository[Invoice]()

    def get_invoice_by_id(self, invoice_id):
        return self.invoice_repository.get([Invoice.id == invoice_id])

    def get_all_invoices(self):
        return self.invoice_repository.get_all()
