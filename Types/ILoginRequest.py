from pydantic import BaseModel

class ILoginRequest(BaseModel):
    username: str
    password: str