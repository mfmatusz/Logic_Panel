from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, time 



class PhoneBase(BaseModel):
    geolocation: Optional[int]
    # status: bool = True
    timestatus: Optional[datetime] = None
    # group_id: Optional[int]

class PhoneCreate(PhoneBase):
    pass

class Phone(PhoneBase):
    id_phone: int
    class Config:
        orm_mode = True
        # Dodaj konwerter dla obiektów time
        json_encoders = {
            datetime.time: lambda v: v.strftime('%H:%M:%S') if v else None
        }
class PhoneTwo(PhoneBase):
    id_phone: int

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }
                
class StatusPayload(PhoneBase):
    id_phone: str
    battery: int
    X_coordinate: str
    Y_coordinate: str
    geolocation: int
    battery: int