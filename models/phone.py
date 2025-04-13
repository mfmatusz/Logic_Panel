from sqlalchemy import Column, Integer, Boolean, Time, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base

class Phone(Base):
    __tablename__ = "phones"

    id_phone = Column(Integer, primary_key=True, index=True)
    geolocation = Column(Integer)
    X_coordinate = Column(String(20))
    Y_coordinate = Column(String(20))
    timestatus = Column(Time)
    is_active = Column(Boolean, default=True)
    battery = Column(Integer, default=100)
    # group_id = Column(Integer, ForeignKey("groups.id_group"))

    # group = relationship("Group", back_populates="phones")
    incidents_triggered = relationship("Incident", back_populates="trigger_phone")