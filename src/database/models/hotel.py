from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import  AuditCreation
from database.orm import Base
"""
Author: Hoang Le Thuy Hoa
"""
class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer ,  primary_key= True, autoincrement=True, nullable=False)
    name = Column(String(255))
    address = Column(String(255))
    phone = Column(String(255))

    def __repr__(self):
        return f"{self.__class__.__name__}"
