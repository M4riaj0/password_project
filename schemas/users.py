from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id_user: Optional[int] = None
    username: str = Field(min_length=2, max_length=15)
    length: int = Field(..., gt=7, lt=20)
    mayus: Optional[bool] = False
    minus: Optional[bool] = False
    numbers: Optional[bool] = False
    symbols: Optional[bool] = False