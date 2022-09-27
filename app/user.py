from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    login: str
    pswd: str
    name: str
    fan_fictions_id: list[int] = None