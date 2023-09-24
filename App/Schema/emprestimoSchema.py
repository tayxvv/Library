from pydantic import BaseModel

from typing import Optional

class emprestimoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    idObra: int

    class Config:
        orm_mode = True

