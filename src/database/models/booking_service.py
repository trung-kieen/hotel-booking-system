from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database.orm import Base


class BookingService(Base):
    __tablename__ = "booking_services"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"))
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    quantity = Column(Integer, default=0, nullable=False)

    # Quan hệ với bảng Service
    service = relationship("Service", back_populates="services_invoices")

    # Quan hệ với bảng Booking
    booking = relationship("Booking", back_populates="services")

    __table_args__ = (
        CheckConstraint(quantity >= 0, name='CK_quantity_positive'),
        {}
    )

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"service_id={self.service_id}, invoice_id={self.booking_id}, "
                f"quantity={self.quantity})>")
