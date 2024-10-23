from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database.orm import Base


class ServiceInvoice(Base):
    __tablename__ = "services_invoices"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"))
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    quantity = Column(Integer, default=0, nullable=False)

    # Relationships
    service = relationship("Service", back_populates="services_invoices")
    invoice = relationship("Invoice", back_populates="services")

    __table_args__ = (
        CheckConstraint(quantity >= 0, name='CK_quantity_positive'),
        {}
    )

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"service_id={self.service_id}, invoice_id={self.invoice_id}, "
                f"quantity={self.quantity})>")
