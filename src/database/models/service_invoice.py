from sqlalchemy import DECIMAL, CheckConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, relationship

from database.orm import Base

class ServiceInvoice(Base):
    __tablename__ = "services_invoices"
    id = Column(Integer ,  primary_key= True, autoincrement=True, nullable=False)
    service_id  = Column(Integer , ForeignKey("services.id"))
    service = relationship("Service" , backref = "services")


    # Many to one
    invoice_id  = Column(Integer , ForeignKey("invoices.id"))
    invoice = relationship("Invoice" , backref = "invoices")

    quantity = Column(Integer() , default= 0 , nullable= False)


    __table_args__ = (
        CheckConstraint(quantity >= 0, name='CK_quantity_positive'),
        {})

    def __repr__(self):
        return f"{self.__class__.__name__}"
