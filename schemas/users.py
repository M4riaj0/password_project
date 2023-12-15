from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id_user: Optional[int] = None
    username: str = Field(min_length=2, max_length=15)
    password: str = Field(min_length=3, max_length=20)