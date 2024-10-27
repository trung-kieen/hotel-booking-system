import enum
from datetime import datetime

from sqlalchemy import DECIMAL, CheckConstraint, Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from database.models.audit import AuditCreation
from database.orm import Base


class PaymentStatus(enum.Enum):
    Done = "Done"
    Pending = "Pending"


class Invoice(Base, AuditCreation):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    total_price = Column(DECIMAL(), nullable=False, default=0)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    prepaid = Column(DECIMAL(), nullable=False, default=0)

    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.Pending)
    # One-to-One relationship with Booking

    booking = relationship("Booking", back_populates="invoice")

    completed_at = Column(DateTime(timezone=True), nullable=True)
    __table_args__ = (
        CheckConstraint(total_price >= 0, name='CK_total_price_positive'),
        {}
    )

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"total_price={self.total_price} "
                f"booking_id={self.booking_id})>")
