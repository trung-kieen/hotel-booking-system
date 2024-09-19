from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import  AuditCreation
from database.orm import Base
"""
Author: Dang Xuan Lam
"""
class BedRoom(Base):
    __tablename__ = "bed_rooms"

    id = Column(Integer, primary_key=True)
    bed_type_id = Column(Integer, ForeignKey("bed_types.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))


    def __repr__(self):
        return f"{self.__class__.__name__}"

