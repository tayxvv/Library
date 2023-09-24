from pydantic import BaseModel

from typing import Optional

class tipoUsuarioSchema(BaseModel):
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True

