from typing import List
from pydantic import BaseModel, Field

class DeviceStatusSchema(BaseModel):
    ClientId: str = Field(alias='client_id')
    ClientName: str = Field(alias='client_name')
    LastDataTimeStamp: int = Field(alias='last_data_timestamp')


class DeviceStatusRequestSchema(BaseModel):
    from_ts: int
    to_ts: int


class DataMessageSchema(BaseModel):
    data: List[BaseModel]
    message: str


class ReponseSchema(BaseModel):
    success: str
    result: DataMessageSchema

