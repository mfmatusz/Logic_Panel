from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.base import Base
import datetime

class Incident(Base):
    __tablename__ = "incidents"

    id_incident = Column(Integer, primary_key=True, index=True)
    X_coordinate = Column(String(20))
    Y_coordinate = Column(String(20))
    confidence = Column(Integer)
    confirmed = Column(Boolean, default=False)
    battery = Column(Integer)
    # group_id = Column(Integer, ForeignKey("groups.id_group"))
    trigger_phone_id = Column(Integer, ForeignKey("phones.id_phone"))
    photo = Column(String(255))
    time = Column(DateTime, default=datetime.datetime.utcnow)

    # group = relationship("Group", back_populates="incidents")
    trigger_phone = relationship("Phone", back_populates="incidents_triggered")
