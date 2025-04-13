from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class IncidentBase(BaseModel):
    # group_id: int
    trigger_phone_id: int
    photo: Optional[str]

class IncidentCreate(IncidentBase):
    pass

class Incident(IncidentBase):
    id_incident: int
    time: datetime

    class Config:
        orm_mode = True
