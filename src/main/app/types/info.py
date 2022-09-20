from pydantic import BaseModel

class UserInfo(BaseModel):
    id: int
    name: str
    patronymic: str | None
    surname: str | None