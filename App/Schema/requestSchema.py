from pydantic import BaseModel

from typing import Optional

class requestSchema(BaseModel):
    token: str

    class Config:
        orm_mode = True