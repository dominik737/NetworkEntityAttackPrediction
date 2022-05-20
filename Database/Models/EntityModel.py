from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from Database.DeclarativeBase import BASE


class EntityModel(BASE):
    __tablename__ = 'Entities'

    id = Column(Integer, primary_key=True)
    identification = Column(String)
    identification_type = Column(Integer)
    FMP_score = Column(Float)
    last_attack_date_time = Column(DateTime)
    last_updated_date_time = Column(DateTime)
    security_events = relationship("SecurityEventModel", back_populates="entity")

