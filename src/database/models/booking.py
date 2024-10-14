from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import AuditCreation
from database.orm import Base


class Booking(Base, AuditCreation):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", backref="customers")

    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=True)

    num_adults = Column(Integer, default=0, nullable=False)

    num_children = Column(Integer, default=0, nullable=False)

    room_id = Column(Integer, ForeignKey("rooms.id"))
    room = relationship("Room", backref="rooms")

    is_canceled = Column(Boolean, default=False, nullable=False)

    __table_args__ = (
        CheckConstraint(num_children >= 0, name='CK_num_children_positive'),
        CheckConstraint(num_adults >= 0, name='CK_num_adults_positive'),
        {})

    def __repr__(self):
        return f"{self.__class__.__name__}"
