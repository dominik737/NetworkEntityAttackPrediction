from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from Communication.Model.SecurityEvent import SecurityEvent
from Evaluation import Normalizator
from Database.DeclarativeBase import BASE


class SecurityEventModel(BASE):
    __tablename__ = 'SecurityEvents'

    def __init__(self, event: SecurityEvent):
        self.attacker_ip = event.attackerIP
        self.detection_date_time = event.detectionTime
        self.victim_ip = event.victimIP
        self.victim_port = event.victimPort
        self.type = Normalizator.get_security_event_type(event.type)
        self.sub_type = Normalizator.get_security_event_sub_type(event.subType)
        self.volume = Normalizator.get_security_event_volume(event.detail, self.type, self.sub_type)
        self.weight = Normalizator.get_security_event_weight(self.type, self.sub_type)
        self.reporterId = event.reporterId
        super().__init__()

    id = Column(Integer, primary_key=True)
    attacker_ip = Column(String)
    detection_date_time = Column(DateTime)
    victim_ip = Column(String)
    victim_port = Column(String)
    type = Column(Integer)
    sub_type = Column(Integer)
    volume = Column(Float)
    weight = Column(Float)
    reporterId = Column(String)
    entity_id = Column(Integer, ForeignKey('Entities.id'))
    entity = relationship("EntityModel", back_populates="security_events")

