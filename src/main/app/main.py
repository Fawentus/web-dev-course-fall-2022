from fastapi import FastAPI
from .types import info

app = FastAPI()

@app.get("/")
def root():
    return {}

@app.get("/hello_world/")
def hello_world():
    return "Hello, world!"

@app.get("/name/{name}")
def name(name: str):
    return {"name": name}

@app.get("/full_name/")
def full_name(name: str, patronymic: str | None = None, surname: str | None = None):
    if patronymic:
        if surname:
            return {"name": name, "patronymic": patronymic, "surname": surname}
        return {"name": name, "patronymic": patronymic}
    if surname:
            return {"name": name, "surname": surname}
    return {"name": name}

@app.post("/user_information/")
def user_information(info: info.UserInfo):
    if info.patronymic and info.surname:
        return "Everything all right"
    return "Insufficient data"