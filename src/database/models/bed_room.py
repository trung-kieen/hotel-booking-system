"""
Author: Dang Xuan Lam
"""
from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import  AuditCreation
from database.orm import Base
class BedRoom(Base):
    __tablename__ = "bed_rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bed_type_id = Column(Integer, ForeignKey("bed_types.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    bed_amount = Column(Integer, nullable=False, default=1)
    __table_args__ = (
        CheckConstraint(bed_amount>= 1, name='CK_bed_amount_positive'),
        {})


    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"bed_type_id={self.bed_type_id}, room_id={self.room_id}, "
                f"bed_amount={self.bed_amount})>")
