from pydantic import BaseModel, Field
from typing import Optional

class Password(BaseModel):
    id_password: Optional[int] = None
    length: int = Field(..., gt=7, lt=20)
    mayus: Optional[bool] = False
    minus: Optional[bool] = False
    numbers: Optional[bool] = False
    symbols: Optional[bool] = False