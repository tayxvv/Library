from pydantic import BaseModel

from typing import Optional

class enderecoSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str

    class Config:
        orm_mode = True

