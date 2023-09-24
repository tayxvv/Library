from pydantic import BaseModel

from typing import Optional

class autorSchema(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True
