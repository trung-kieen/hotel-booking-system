"""
Author: Hoang Le Thuy Hoa
"""
from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import  AuditCreation
from database.orm import Base
class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer ,  primary_key= True, autoincrement=True, nullable=False)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    date = Column(DateTime)
    content = Column(String(255))
    rate = Column(Integer) # 1 -> 5

    # One to one
    booking = relationship("Booking", backref=backref("reviews", uselist=False))

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"booking_id={self.booking_id}, date={self.date}, "
                f"rate={self.rate}, content='{self.content[:20]}...')>")
