from pydantic import BaseModel

from typing import Optional

class usuarioSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    username: str
    password: str

    class Config:
        orm_mode = True

