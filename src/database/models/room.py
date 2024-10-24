"""
Author: Nguyen Khac Trung Kien
"""
import enum

from sqlalchemy.orm import backref, defaultload, relationship
from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey, Enum

from database.models.audit import AuditCreation
from database.orm import Base

"""
Author: Dang Xuan Lam
"""


class RoomType(enum.Enum):
    Standard = "Standard"
    Deluxe = "Deluxe"
    Suit = "Suit"

    def __str__(self):
        return self.name


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    floor_id = Column(Integer, ForeignKey("floors.id"), nullable=False)
    room_type = Column(Enum(RoomType), nullable=False)
    is_locked = Column(Integer, default=0, nullable=False)
    price = Column(DECIMAL, default=0, nullable=False)
    bed_types = relationship("BedType", secondary="bed_rooms", back_populates="rooms", )

    # Cascade allow to delete room if there are no
    bookings = relationship("Booking", back_populates="room" , cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(price> 0, name='CK_total_price_positive'),
        {})
    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"floor_id={self.floor_id}, room_type='{self.room_type}', "
                f"is_locked={self.is_locked}, price={self.price})>")
