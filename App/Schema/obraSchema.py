from pydantic import BaseModel

from typing import Optional

class obraSchema(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True

