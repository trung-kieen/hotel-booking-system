

from sqlalchemy import DECIMAL, CheckConstraint, Column, Date, Enum, Integer, String, ForeignKey, func
from sqlalchemy.orm import Relationship, backref, relationship
from enum import Enum as enum

from database.models.audit import  AuditCreation
from database.orm import Base


class Gender(enum):
    FEMALE = 0
    MALE  = 1


class Customer(Base, AuditCreation):
    __tablename__ = "customers"
    id = Column(Integer ,  primary_key= True)


    firstname = Column(String(80), nullable= False )
    lastname = Column(String(50), nullable= False )
    address = Column(String(200)  )


    birth  = Column (Date())

    gender  = Column (Enum(Gender))


    # TODO: revise contraint
    phone = Column(String (13))

    email =  Column(String ( 50 ))

    __table_args__ = (
        CheckConstraint(birth  < func.current_date() , name='CK_birthdate_in_past'),
        {})




    def __repr__(self):
        return f"{self.__class__.__name__}"