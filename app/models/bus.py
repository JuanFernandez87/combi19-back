from sqlalchemy import(
    Column,  
    Integer, 
    String, 
    ForeignKey
)
from ..database import Base
from sqlalchemy.orm import relationship

class Bus(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(255))
    patent = Column(String(255))
    number_of_seats = Column(Integer)
    type_of_service = Column(String(255))
    driver_id = Column(Integer, ForeignKey('user.id'))
    
    # many-to-one side remains, see tip below
    user = relationship('User', back_populates='bus')