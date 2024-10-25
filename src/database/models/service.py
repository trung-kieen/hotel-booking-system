from sqlalchemy import DECIMAL, CheckConstraint, Column, Integer, String
from sqlalchemy.orm import relationship
from database.orm import Base


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    price = Column(DECIMAL, nullable=False, default=0)

    # Quan hệ với bảng BookingService
    services_invoices = relationship("BookingService", back_populates="service")

    __table_args__ = (
        CheckConstraint(price >= 0, name='CK_price_positive'),
        {})

    def __repr__(self):
        return (f"<{self.__class__.__name__}(id={self.id}, "
                f"name='{self.name}', price={self.price})>")
