from pydantic import BaseModel, validator, Field
from typing import List, Optional, Iterable
from dashboard.constants import Periods


class FetchHistogramInput(BaseModel):
    ClientId: str = Field(alias="client_id")
    Timestamp: int = Field(alias="timestamp")
    Period: str = Field(Periods.WeeklyGroup, alias="period")
    ToTimeStamp: Optional[int] = Field(alias="to_ts")
    FromTimeStamp: Optional[int] = Field(alias="from_ts")

    @validator('Period', pre=True, always=True)
    def period_check(cls, v: str) -> str:
        if v not in Periods.get_all_periods():
            return Periods.WeeklyGroup
        return v


class ElectricalDataSchema(BaseModel):
    ClientId: str = Field(alias='client_id')
    VoltageRMS: float = Field(alias='voltage_rms')
    CurrentRMS: float = Field(alias='current_rms')
    AveragePower: float = Field(alias='average_power')
    EnergyConsumption: float = Field(alias='energy_consumption')
    GenerationTimeStamp: int = Field(alias='generation_time_stamp')
    DeleteStatus: bool = Field(alias='delete_status')

    class Config:
        orm_mode = True


class TimestampAndValueObjectSchema(BaseModel):
    Timestamp: int = Field(alias='timestamp')
    Value: float =  Field(alias='value')

class SuccessMessage(BaseModel):
    Message: str = Field(alias='message')
    Success: bool = Field(alias='success')

class HistogramOutput(SuccessMessage):
    Data: List[TimestampAndValueObjectSchema] = Field(alias='data')
