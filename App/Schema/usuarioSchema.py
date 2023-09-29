from pydantic import BaseModel

from typing import Optional

class usuarioSchema(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    username: str
    password: str

    class Config:
        orm_mode = True

