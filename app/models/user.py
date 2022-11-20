from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime
)
from ..database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String(255))
    firstname = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(100))
    password = Column(String(255))
    date_of_birth = Column(DateTime)
    activated = Column(Integer)
    admin = Column(Integer)
    chofer = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # one-to-one User.bus
    bus = relationship("Bus", back_populates="user", uselist=False)
