
from sqlalchemy import DECIMAL, CheckConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, relationship

from database.models.audit import  AuditCreation
from database.orm import Base

class Invoice(Base, AuditCreation):
    __tablename__ = "invoices"
    id = Column(Integer ,  primary_key= True)

    total_price  = Column(DECIMAL(), nullable= False, default= 0 )

    quantity = Column(Integer() )

    booking_id = Column(Integer , ForeignKey("bookings.id"))
    # One to one relationship
    booking= relationship("Booking" , backref=backref("bookings", uselist=False))

    __table_args__ = (
        CheckConstraint(total_price >= 0, name='CK_total_price_positive'),
        {})

    def __repr__(self):
        return f"{self.__class__.__name__}"
