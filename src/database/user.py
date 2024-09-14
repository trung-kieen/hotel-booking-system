

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship

from database.models.audit import Audit
from database.orm import Base

class User (Base, Audit):
    __tablename__ = "users"
    id = Column(Integer ,  primary_key= True)
    firstname = Column (String(80) , nullable = False  )
    lastname = Column (String(80) , nullable = False  )
    email = Column (String(80) , nullable = False  , unique = True)
#    preference = Relationship ( "Preference", back_populates= "user")

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.firstname} {self.lastname}"
