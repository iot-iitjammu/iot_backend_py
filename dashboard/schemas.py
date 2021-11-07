from pydantic import BaseModel, validator
from typing import Optional
from dashboard.constants import Periods


class FetchHistogramInput(BaseModel):
    ClientId: str
    Timestamp: int
    Period: Optional[str]
    ToTimeStamp: Optional[int]
    FromTimeStamp: Optional[int]
    
    @validator('Period', pre=True, always=True)
    def period_check(cls, v: Optional[str]) -> str:
        if v not in Periods.get_all_periods():
            return Periods.WeeklyGroup
        return v
        
class ElectricalData(BaseModel):
    ClientId: str
    VoltageRMS: float
    CurrentRMS: float
    AveragePower: float
    EnergyConsumption: float
    GenerationTimeStamp: int
    DeleteStatus: bool

class TimestampAndValueObject(BaseModel):
    Timestamp: int
    Value: float
