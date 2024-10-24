

from sqlalchemy import DECIMAL, CheckConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship

from database.orm import Base

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer ,  primary_key= True, autoincrement=True)
    name = Column( String(80),nullable= False )
    price = Column ( DECIMAL  ,  nullable= False , default= 0)
    services_invoices = Relationship("ServiceInvoice", back_populates="service")
    __table_args__ = (
        CheckConstraint(price >= 0, name='CK_price_positive'),
        {})

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"name='{self.name}', price={self.price})>")

