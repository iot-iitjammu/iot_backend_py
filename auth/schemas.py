from pydantic import BaseModel
from typing import Optional

class AuthCallbackSchema(BaseModel):
    code: str
    redirect_uri: str

class Tokens(BaseModel):
    id_token: str
    access_token: str

class CallbackResponse(BaseModel):
    tokens: Optional[Tokens]
    status: bool
    message: str

