import enum

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import AuditCreation
from database.orm import Base


class BookingType(enum.Enum):
    Hourly = "Hourly"
    Daily = "Daily"


class Booking(Base, AuditCreation):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, autoincrement=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", backref="customers")

    start_date = Column(DateTime, nullable=False)

    checkin = Column(DateTime, nullable=True)

    checkout = Column(DateTime, nullable=True)

    end_date = Column(DateTime, nullable=False)

    num_adults = Column(Integer, default=0, nullable=False)

    num_children = Column(Integer, default=0, nullable=False)

    room_id = Column(Integer, ForeignKey("rooms.id"))

    room = relationship("Room", backref="rooms")

    is_canceled = Column(Boolean, default=False, nullable=False)

    booking_type = Column(Enum(BookingType), nullable=False, default=BookingType.Daily)

    invoice = relationship("Invoice", uselist=False, back_populates="booking", foreign_keys="Invoice.booking_id")

    services = relationship("BookingService", back_populates="booking")
    
    

    __table_args__ = (
        CheckConstraint(num_children >= 0, name='CK_num_children_positive'),
        CheckConstraint(num_adults >= 0, name='CK_num_adults_positive'),
        {})

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"customer_id={self.customer_id}, start_date={self.start_date}, "
                f"checkin={self.checkin}, checkout={self.checkout}, "
                f"end_date={self.end_date}, num_adults={self.num_adults}, "
                f"num_children={self.num_children}, room_id={self.room_id}, "
                f"is_canceled={self.is_canceled})>")
