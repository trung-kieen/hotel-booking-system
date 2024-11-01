"""
Author: Dang Xuan Lam
"""
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database.orm import Base


class BookingService(Base):
    __tablename__ = "booking_services"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"))
    booking_id = Column(Integer, ForeignKey("bookings.id"))

    # # Quan hệ với Service và Booking
    # service = relationship("Service", backref="booking_services")
    # booking = relationship("Booking", backref="booking_services")

    __table_args__ = (
        {}
    )

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"service_id={self.service_id}, invoice_id={self.booking_id}, "
                f"quantity={self.quantity})>")
